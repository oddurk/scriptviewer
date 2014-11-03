from SingletonType import SingletonType

class FileContainer(object):
    __metaclass__ = SingletonType
    def __init__(self):
        super(FileContainer, self).__init__()
        self._filesParsed = set()

    def addFile(self, file):
        self._filesParsed.add(file)

    def hasBeenParsed(self, file):
        if file in self._filesParsed:
            return True
        else:
            return False
