from filetree import FileContainer

## File tree item.
# An recursive structure of FileTrees
class FileTree(object):

    ## The constructor
    #
    # @param self The object pointer.
    # @pararm filecontainer The file to store in the tree.
    def __init__(self, filecontainer):
        if not isinstance(filecontainer, FileContainer):
            raise TypeError("filelinelocation must be a FileLineLocation object.")

        self._filecontainer = filecontainer
        self._children = {}

    def addchild(self, filetree, line):
        self._children[line] = filetree

    def printTree(self, line=0):
        print "I am: " + str(line) + ": " + str(self._filecontainer)
        for item in sorted(self._children.keys()):
            self._children[item].printTree(item)

    def getfilecontainer(self):
        return self._filecontainer

    def getNode(self, filecontainer):
        if filecontainer == self._filecontainer:
            return self
        for item in self._children.keys():
            if self._children[item].getfilecontainer() == filecontainer:
                return self._children[item]
        for item in self._children.keys():
            if self._children[item].getNode(filecontainer) is not None:
                self._children[item].getNode(filecontainer)
        return None

    def addLink(self, fromfile, tofile, line=0):
        if not isinstance(fromfile, FileContainer):
            raise TypeError("fromfile must be a FileContainer")
        if not isinstance(tofile, FileContainer):
            raise TypeError("tofile must be a FileContainer")

        ft = self.getNode(fromfile)

        if ft is not None:
            ft.addchild(FileTree(tofile), line)
        else:
            print "Did not find the file in the tree."


    def __str__(self):
        return self._filecontainer.getfilename() + ":" + str(self._children)

    def __repr__(self):
        return self.__str__()