from SingletonType import SingletonType
import matplotlib.pyplot as plt
import networkx as nx

class Plotter(object):
    @staticmethod
    def plotGraph(graph):
        pos = nx.spring_layout(graph, k=0.3) # positions for all nodes
        nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='#ffffff')
        nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(data=True), width=1, arrows=True)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_family='sans-serif')

        plt.axis('off')
        plt.show() # display