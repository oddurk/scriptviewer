from SingletonType import SingletonType
## Container for files which have been parsed
# Singleton class for files
class FileStore(object):
    __metaclass__ = SingletonType
    ## The constructor
    #
    # @param self The object pointer.
    def __init__(self):
        super(FileStore, self).__init__()
        self._filesParsed = set()

    ## Adds a file to the file container
    #
    # @param self The object poniter.
    # @param file The file to be added.
    def addFile(self, file):
        self._filesParsed.add(file)

    ## Accessor to the file container.
    #
    # @param self The object pointer.
    # @param file The file to locate in the file container.
    # @return True if the file has been parsed, false if not
    def hasBeenParsed(self, file):
        if file in self._filesParsed:
            return True
        else:
            return False