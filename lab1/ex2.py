import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

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
    nodes = calculate_nodes_position(len(matrix))
    plt.figure(figsize=(5, 5))
    graph_visualization = nx.from_numpy_matrix(matrix)
    nx.draw_networkx(graph_visualization, nodes)
    plt.show()

#test from example from kotfica's pdf
create_graph_visualization(array)