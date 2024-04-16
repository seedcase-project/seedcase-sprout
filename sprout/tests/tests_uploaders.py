import io
import os

from django.test import TestCase

from config.settings import PERSISTENT_STORAGE_PATH
from sprout.helpers.paths import path_raw_storage
from sprout.uploaders import write_to_raw


class TestUploadRawDataFile(TestCase):
    def setUp(self):
        self.file = io.BytesIO(b"A file with some content")
        self.file.name = "fake-test-file.csv"
        self.expected_file = "fake.test.csv"
        self.expected_path = os.path.join(path_raw_storage(0), self.expected_file)

    def test_write_to_raw(self):
        result_path = write_to_raw(self.file, self.expected_file)
        self.assertEqual(result_path, self.expected_path)
        self.assertTrue(os.path.isfile(self.expected_path))

    def tearDown(self):
        # Clean up created file after test
        os.remove(self.expected_path)
