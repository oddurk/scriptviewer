from SingletonType import SingletonType
import networkx as nx
## filegraph
# A singleton class container for the file graph.
class FileGraph(object):
    __metaclass__ = SingletonType

    ## The constructor.
    #
    # @param self The object pointer.
    def __init__(self):
        self._graph = nx.DiGraph()

    ## Adds an (directed) edge between nodes.
    #
    # @param self The object pointer.
    # @param edgeFrom The node from which the edge connected.
    # @param edgeTo The edge to the node to be connected.
    def add_edge(self, edgeFrom, edgeTo):
        self._graph.add_edge(edgeFrom, edgeTo)


    ## Getter for the graph to be used
    #
    # @param self The object pointer.
    def getGraph(self):
        return self._graph
