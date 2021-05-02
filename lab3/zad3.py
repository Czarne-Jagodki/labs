from typing import List
from Github.lab3.zad1 import graph
from Github.lab3.zad2 import dijkstra
from Github.structures.Graph import Graph


def create_distances_matrix(g: Graph) -> List[List[int]]:
    """
    Funkcja tworzy i zwraca macierz odleglosci
    """
    matrix = [[0 for v in g.get_vertices()] for v in g.get_vertices()]
    list_of_vertices = [x.get_id() for x in g.get_vertices()]
    for start_vertex in list_of_vertices:
        # wywolujemy dijkstre na kazdym wierzcholku znajdujac najkrotsze odleglosci dla kazdej pary wierzcholkow
        distances, predecessors = dijkstra(g, start_vertex)
        for end_vertex, distance in distances.items():
            # macierz odleglosci - najkrotsza odleglosc od wierzcholka start_vertex do wierzcholka end_vertex
            matrix[start_vertex][end_vertex] = distance

    return matrix


def main():
    print("\nZestaw 3, zadanie 3 - macierz odległości:")
    distances_matrix = create_distances_matrix(graph)
    for row in distances_matrix:
        print(*row, sep='\t')


if __name__ == "__main__":
    main()
