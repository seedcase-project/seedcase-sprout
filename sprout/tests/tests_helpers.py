import pathlib

from django.test import TestCase

from sprout.helpers.paths import (
    path_database_dir,
    path_database_file,
    path_project_storage,
    path_raw_storage,
)


class HelperPaths(TestCase):
    def test_path_database_file(self):
        self.assertEqual(
            path_database_file(999),
            pathlib.Path(path_database_dir(999), "project_database.db"),
        )

    def test_path_database_dir(self):
        self.assertEqual(
            path_database_dir(999),
            pathlib.Path(path_project_storage(), "999", "databases"),
        )

    def test_path_raw_storage(self):
        self.assertEqual(
            path_raw_storage(999),
            pathlib.Path(path_project_storage(), "999", "raw"),
        )

    def test_path_project_storage(self):
        self.assertEqual(
            path_project_storage(),
            pathlib.Path("persistent_storage", "project"),
        )

    def tearDown(self):
        path_database_file(999).rmdir()
        path_database_dir(999).rmdir()
