from SingletonType import SingletonType
from filetree import FileTree
from filetree import FileContainer

## FileGraph
# A singleton class container for the file graph.
class FileGraph(object):
    __metaclass__ = SingletonType

    ## The constructor.
    #
    # @param self The object pointer.
    def __init__(self, file):
        self._graph = FileTree(FileContainer(file))

    ## Adds an (directed) edge between nodes.
    #
    # @param self The object pointer.
    # @param edgeFrom The node from which the edge connected.
    # @param edgeTo The edge to the node to be connected.
    def add_edge(self, edgeFrom, edgeTo, line=0):
        self._graph.addLink(edgeFrom, edgeTo, line)

    ## Getter for the graph to be used
    #
    # @param self The object pointer.
    def getGraph(self):
        return self._graph
