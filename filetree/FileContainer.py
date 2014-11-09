from debug import Debug


## Container for files.
# Initially, it only contains the location and the name of the file.
# When needed the file can be loaded.
# File paths are assumed to be absolute.
class FileContainer(object):

    ## The constructor
    #
    # @param self The object pointer.
    # @param file_name The name of the file.
    # @param file_directory The directory of the file.
    def __init__(self, file=""):
        self._file = file
        self._file_read = False
        self._lines = []

    ## Read the file from disk to memory, void.
    #
    # @param self The object pointer
    def readfile(self):
        if not self._file_read:
            Debug().dev("Reading file")
            f = open(self._file)
            for line in f:
                self._lines.append(line.strip())
            f.close()
            self._file_read = True

    ## Prints the file to screen, void.
    #
    # @self The object pointer.
    def printfile(self):
        for item in self._lines:
            print item

    ## Getter for file name
    #
    # @param self The object pointer.
    # @return The file name, as string.
    def getfilename(self):
        return self._file

    ## The equality operator
    #
    # @param self The object pointer.
    # @param other The object to compare.
    # @return True if the file and directories are the same.
    def __eq__(self, other):
        return self.getfilename() == other.getfilename()

    ## The string representation.
    #
    # @param self The object pointer.
    # @return The string representation; folder / file.
    def __str__(self):
        return ".." + self._file[-20:]

    ## The object representation.
    #
    # @param self The object pointer.
    # @return Calls the __str__ method.
    def __repr__(self):
        return self.__str__()