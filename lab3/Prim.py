import numpy as np
from zad1 import create_rand_consistent_weighted_graph, draw
from ex2 import create_graph_visualization
from random import randrange
from collections import namedtuple
from Graph import Graph
from Vertex import Vertex
from Edge import Edge

EdgePrim = namedtuple('EdgePrim', 'from_vertex to_vertex weight');

class GraphPrim:
    def __init__(self, neighborhood_matrix, weight_matrix):
        self.n_matrix = neighborhood_matrix
        self.weight_matrix = weight_matrix

def edges_and_vertices_to_adjacency_matrix(edges: list, vertices: list) -> list:
    matrix = list()
    
    for i in range(len(vertices)):
        matrix.append(list())
        for j in range(len(vertices)):
            matrix[i].append(0)
    
    for edge in edges:
        matrix[edge.vertices[0].id][edge.vertices[1].id] = 1
        matrix[edge.vertices[1].id][edge.vertices[0].id] = 1
        
    return matrix

def edges_and_vertices_to_weights_matrix(edges: list, vertices: list) -> list:
    matrix = list()
    
    for i in range(len(vertices)):
        matrix.append(list())
        for j in range(len(vertices)):
            matrix[i].append(0)
            
    for edge in edges:
        matrix[edge.vertices[0].id][edge.vertices[1].id] = edge.get_weight()
        matrix[edge.vertices[1].id][edge.vertices[0].id] = edge.get_weight()
        
    return matrix

def convert_to_drawable_graph(graphPrim: GraphPrim, edgesPrim: list) -> Graph:
    graph = Graph(weighted=True)
    edges = set()
    
    for i in range(len(graphPrim.n_matrix)):
        graph.add_vertex(Vertex(i))
        
    for edge in edgesPrim:
        edges.add((Vertex(edge.from_vertex), Vertex(edge.to_vertex), edge.weight))
        
    graph.add_edges(edges)
    
    return graph

def get_random_weights(num_of_vertexes: int) -> list:
    weights = list()
    for i in range(num_of_vertexes):
        weights.append(list())
        for j in range(num_of_vertexes):
            if i != j:
                weights[i].append(randrange(10) + 1)
            else:
                weights[i].append(0)            
    return weights

def get_min_vertice(vertices: list) -> EdgePrim:
    min_vertice_index = 0
    
    for i in range(1, len(vertices)):
        if vertices[i].weight < vertices[min_vertice_index].weight:
            min_vertice_index = i
            
    return vertices[min_vertice_index]
    
    
# znajduje drzewo rozpinajace algorytmem Prima, zwraca drzewo rozpinajace
# w postaci listy krawedzi
def find_spanning_tree(graph: GraphPrim, starting_vertex: int) -> list:    
    NUM_OF_VERTICES = len(graph.n_matrix)
    tree = [starting_vertex]
    vertices = list(range(0, NUM_OF_VERTICES))
    vertices.remove(starting_vertex)
    edges = list()
    
    while len(tree) < NUM_OF_VERTICES:
        lightest_weight = None
        current_edge = None
        chosen_vertex = None
        
        for from_vertex in tree:
            for to_vertex in vertices:
                if graph.n_matrix[from_vertex][to_vertex] == 1:
                    current_weight = graph.weight_matrix[from_vertex][to_vertex]
                    if lightest_weight is None or current_weight < lightest_weight: 
                        lightest_weight = current_weight
                        current_edge = EdgePrim(from_vertex, to_vertex, current_weight)
                        chosen_vertex = to_vertex
                    
        tree.append(chosen_vertex)
        # print(chosen_vertex)    
        edges.append(current_edge)
        vertices.remove(chosen_vertex)
            
    return edges;

def prepare_spanning_matrix(edges: list, num_of_vertices: int) -> list:
    tree_matrix = list()
    for i in range(num_of_vertices):
        tree_matrix.append(list())
        for j in range(num_of_vertices):
            tree_matrix[i].append(0)
            
    for edge in edges:
        tree_matrix[edge.from_vertex][edge.to_vertex] = 1
        
    return tree_matrix


if __name__ == '__main__':
    random_graph = create_rand_consistent_weighted_graph(n=7, weight_min=1, 
                                                         weight_max=10)
    
    adj_matrix = edges_and_vertices_to_adjacency_matrix(random_graph.get_edges(), 
                                                        random_graph.get_vertices())
    
    weights_matrix = edges_and_vertices_to_weights_matrix(random_graph.get_edges(),
                                                          random_graph.get_vertices())
    draw(random_graph)
    
    graphPrim = GraphPrim(adj_matrix, weights_matrix)
    edgesPrim = find_spanning_tree(graphPrim, starting_vertex=0)
    
    graph = convert_to_drawable_graph(graphPrim, edgesPrim)
    
    draw(graph)    