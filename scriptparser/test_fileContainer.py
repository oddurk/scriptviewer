from unittest import TestCase
from scriptparser import FileContainer

class TestFileContainer(TestCase):
    def test_addFile(self):
        f = FileContainer()
        f.addFile("file")

        self.assertEqual(size(f._filesParsed), 1)

    def test_hasBeenParsed(self):
        f = FileContainer()
        f.addFile("test")
        self.assertTrue(f.hasBeenParsed("test"))