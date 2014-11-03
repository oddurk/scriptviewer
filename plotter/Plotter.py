from SingletonType import SingletonType
import matplotlib.pyplot as plt
import networkx as nx

class Plotter(object):
    __metaclass__ = SingletonType
    def __init__(self):
        self._graph = nx.DiGraph()

    def add_edge(self, edgeFrom, edgeTo):
        self._graph.add_edge(edgeFrom, edgeTo)


    def plotGraph(self):
        allEdges = [(u,v) for (u,v,d) in self._graph.edges(data=True)]
        pos = nx.spring_layout(self._graph) # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(self._graph, pos, node_size=7000, node_color='#ffffff')

        # edges
        nx.draw_networkx_edges(self._graph, pos, edgelist=allEdges, width=1, arrows=True)

        # labels
        nx.draw_networkx_labels(self._graph, pos, font_size=12, font_family='sans-serif')

        plt.axis('off')
        #plt.savefig("weighted_graph.png") # save as png
        plt.show() # display
