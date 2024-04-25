# db file is created if none exists
# table name in database matches name given
# db table gets created if none exists
# created database rows equal input rows
# created database columns equal input columns
# excluded columns are not included in database
# adding another table with data is saved to same database
# only one db is created for all tables in project
import io
import pathlib

from django.test import TestCase
from django.urls import reverse

from sprout.helpers.paths import path_database_dir, path_database_file
from sprout.models import Columns, Files
from sprout.tests.db_test_utils import create_table


class ProjectMetadataDataCreate(TestCase):
    def setUp(self):
        """Create a table and a column for testing."""
        self.tables = create_table("TestTable")

        file = io.BytesIO(b"TestColumn,Letter\n1,A\n2,B\n3,C\n4,C\n5,C\n6,C")
        file.name = "file-name.csv"
        self.files = Files.create_model(file, self.tables.id)

    def test_database_created(self):
        # Arrange
        # create a file
        # run the data create view

        # Act
        url = reverse("projects-id-metadata-id-data-create", args=[self.tables.id])
        response = self.client.post(url)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(path_database_file(0).exists())

    def test_projects_id_metadata_id_data_create_view_get(self):
        """Test that the page renders."""
        # Arrange
        url = reverse("projects-id-metadata-id-update", args=[self.tables.id])

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects-id-metadata-id-update.html")

    def tearDown(self) -> None:
        """Remove the test database."""
        os.rmdir(path_database_dir(0))
        self.tables.delete()
        Columns.objects.all().delete()
        Files.objects.all().delete()
