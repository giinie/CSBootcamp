from tempfile import TemporaryDirectory
from unittest import TestCase


class MyTest(TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()

    # Test methods follow
