from zad1 import graph, draw
from ex2 import create_graph_visualization
from random import randrange
from collections import namedtuple
from Graph import Graph
from Vertex import Vertex
from Edge import Edge
from typing import List

'''
Named tuple dla reprezentacji krawedzi - uzywane jedynie na potrzeby tego zadania
'''
EdgePrim = namedtuple('EdgePrim', 'from_vertex to_vertex weight');

'''
Prosta klasa w formie struktury do przechowywania macierzy sasiedztwa i wag
grafu wazonego.
'''
class GraphPrim:
    def __init__(self, neighborhood_matrix, weight_matrix):
        self.n_matrix = neighborhood_matrix
        self.weight_matrix = weight_matrix

'''
Funkcja przeksztalca listy obiektow typow Edge i Vertex do jednej z reprezentacji "niskopoziomowych"
tzn. do macierzy sasiedztwa
'''
def edges_and_vertices_to_adjacency_matrix(edges: List[Edge], vertices: List[Vertex]) -> List[list]:
    matrix = list()
    
    for i in range(len(vertices)):
        matrix.append(list())
        for j in range(len(vertices)):
            matrix[i].append(0)
    
    for edge in edges:
        matrix[edge.vertices[0].id][edge.vertices[1].id] = 1
        matrix[edge.vertices[1].id][edge.vertices[0].id] = 1
        
    return matrix

'''
Funkcja przeksztalca listy obiektow typu Edge i Vertex do jednej z reprezentacji "niskopoziomowych"
tzn. do macierzy wag
'''
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

'''
Zadaniem funkcji jest przeksztalcenie grafu z postaci "niskopozimowej" (jako obiektu GraphPrim zlozonego
z macierzy sasiedztwa i macierzy wag oraz listy EdgePrim) do obiektu typu Graph, ktory mozna narysowac
przy pomocy metody pomocniczej do wizualizacji ze skryptu z zadaniem 1.
'''
def convert_to_drawable_graph(graphPrim: GraphPrim, edgesPrim: List[EdgePrim]) -> Graph:
    graph = Graph(weighted=True)
    edges = set()
    
    for i in range(len(graphPrim.n_matrix)):
        graph.add_vertex(Vertex(i))
        
    for edge in edgesPrim:
        edges.add((Vertex(edge.from_vertex), Vertex(edge.to_vertex), edge.weight))
        
    graph.add_edges(edges)
    
    return graph


'''
Dla grafu zadanego w postaci macierzy sasiedztwa i macierzy wag (obiekt typu GraphPrim) oraz dowolnego wybranego
indeksu wierzcholka
funkcja znajduje minimalne drzewo rozpinajace i zwraca je w postaci listy krawedzi (lista obiektow
typu EdgePrim). Jest to przyklad najmniej efektywnej implementacji algorytmu (uzycie macierzy sasiedztwa
oraz zwyklej kolejki priorytetowej (poszukiwanie minimalnej wagi w kolejnych iteracjach)).

Graf musi byc oczywisce spojny, w przeciwnym wypadku nastapi blad (np. usuwanie pustego elementu z listy).
'''    
def find_spanning_tree(graph: GraphPrim, starting_vertex: int) -> List[EdgePrim]:    
    NUM_OF_VERTICES = len(graph.n_matrix)
    tree = [starting_vertex] # tutaj bd przechowywane wierzcholki, ktore jud dodano do rzewa
    vertices = list(range(0, NUM_OF_VERTICES)) # tutaj przechowywane sa wszystkie wierzcholki 
    # ktorych nie dodano jeszcze do budowanego drzewa
    vertices.remove(starting_vertex) # na wstepie musimy usunac z listy niedodanych wierzcholkow wierzcholek startowy
    edges = list() # lista do przechowywania krawedzi
    
    '''
    Algorytm dziala dopoki nie dodano wszystkich wierzcholkow do drzewa.
    '''
    while len(tree) < NUM_OF_VERTICES:
        lightest_weight = None
        current_edge = None
        chosen_vertex = None
        
        '''
        Musimy przeiterowac po wszystkich wierzcholkach juz dodane do drzewa i tymi ktorych jeszcze nie
        dodano. Sprawdzamy czy istnieje miedzy nimi krawedz (linia 108.). Jeli tak, to sprawdzamy czy nowa
        krawedz ma mniejsza wage od uprzednio rozwazanych. Jesli tak to zapisujemy ja jako najlzejsza krawedz
        (current_edge). Po iteracjach zapisujemy do drzewa wiecholek ktory utworzyl najlzejsza krawedz.
        Zapisujemy rowniez sama krawedz na potrzeby zwracanej listy. Z wierzcholkow niedodanych do drzewa
        usuwamy wybrany wierzcholek.
        '''
        for from_vertex in tree:
            for to_vertex in vertices:
                if graph.n_matrix[from_vertex][to_vertex] == 1:
                    current_weight = graph.weight_matrix[from_vertex][to_vertex]
                    if lightest_weight is None or current_weight < lightest_weight: 
                        lightest_weight = current_weight
                        current_edge = EdgePrim(from_vertex, to_vertex, current_weight)
                        chosen_vertex = to_vertex
                    
        tree.append(chosen_vertex) # w kazdej iteracji zewnetrznej petli dolaczamy nowy wierzcholek do drzewa
        edges.append(current_edge) # do listy krawedzi stanowiacej rezultat dzialania algorytmu dolaczamy nowa krawedz
        vertices.remove(chosen_vertex) # z listy niedodanych jeszcze wierzcholkow usuwamy
            
    return edges;


if __name__ == '__main__':
    adj_matrix = edges_and_vertices_to_adjacency_matrix(graph.get_edges(), 
                                                        graph.get_vertices())
    
    weights_matrix = edges_and_vertices_to_weights_matrix(graph.get_edges(),
                                                          graph.get_vertices())
    
    graphPrim = GraphPrim(adj_matrix, weights_matrix)
    edgesPrim = find_spanning_tree(graphPrim, starting_vertex=0)
    
    result_graph = convert_to_drawable_graph(graphPrim, edgesPrim)
    
    draw(result_graph, 'result.png')    