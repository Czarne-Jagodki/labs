import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import ex1

array = np.matrix([
                 [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                 [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                 [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
])

def calculate_nodes_position(n_of_nodes):
    nodes = {}
    for n in range(0, n_of_nodes):
        x = math.cos(2 * math.pi / n_of_nodes * n)
        y = math.sin(2 * math.pi / n_of_nodes * n)
        nodes.update({n: (x, y)})
    return nodes

def create_graph_visualization(matrix):
    """
    Function visualizes the matrix of neighbourhood of graph
    :param matrix: it's a numpy matrix, so using our functions from previous module
                    it is needed to be converted by numpy.matrix
    :return: None
    """
    nodes = calculate_nodes_position(len(matrix))
    plt.figure(figsize=(5, 5))
    graph_visualization = nx.from_numpy_matrix(matrix)
    nx.draw_networkx(graph_visualization, nodes)
    plt.show()

#create_graph_visualization(array)

create_graph_visualization(np.matrix(ex1.from_list_to_matrix_neighbour(ex1.neighbour_list)))