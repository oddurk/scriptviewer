from unittest import TestCase
from scriptparser import FileStore

class TestFileContainer(TestCase):
    def test_addFile(self):
        f = FileStore()
        f.addFile("file")

        self.assertEqual(size(f._filesParsed), 1)

    def test_hasBeenParsed(self):
        f = FileStore()
        f.addFile("test")
        self.assertTrue(f.hasBeenParsed("test"))