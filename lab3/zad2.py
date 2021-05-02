import math
from typing import Dict, Tuple, List
from Github.lab3.zad1 import create_rand_consistent_weighted_graph, draw
from Github.structures import Graph


def dijkstra(graph: Graph, start_vertex: int) -> Tuple[Dict[int, int], Dict[int, int]]:
    """
    Znajduje najkrótsze odległość od wejściowego wierzchołka do każdego innego
    :param graph: wejściowy graf
    :param start_vertex: początkowy wierzchołek
    :return: słownik najkrótszych odległości oraz słownik poprzedników wierzchołka
    """

    # poprzednicy wierzcholka
    predecessors = {}

    # najkrotsze odleglosci trasy do wierzcholkow
    distances = {}

    # lista wierzchołkow grafu, kluczem - aktualnie wyliczona odleglosc
    list_of_vertices = []

    vertices = list(graph.get_vertices())  # lista wierzcholkow
    vertices_ids = [v.get_id() for v in vertices]  # lista id wierzcholkow

    # INIT
    for vertex in vertices_ids:
        distances[vertex] = math.inf  # gorne ograniczenie wagi najkrotszej sciezki
        predecessors[vertex] = None  # chwilowy brak poprzednika
        list_of_vertices.append(vertex)
    distances[start_vertex] = 0  # najkrotsza sciezka ze start_vertex do start_vertex

    # iterujemy dopoki zbior wierzcholkow nie bedzie pusty
    while list_of_vertices:
        # usuwamy pierwszy wierzcholek w kazdej iteracji
        list_of_vertices.sort(key=lambda n: distances[n])  # zeby zaczac od start_vertex, czyli od distance=0
        u = list_of_vertices.pop(0)
        for v in graph.find_neighbours(u):
            if v in list_of_vertices:
                edge_weight = graph.find_edge(u, v).get_weight()
                # relaksacja krawedzi - poprawienie rozwiazania
                if distances[v] > distances[u] + edge_weight:
                    distances[v] = distances[u] + edge_weight
                    predecessors[v] = u

    print("Odległości:\n" + str(distances))
    print("Poprzednicy:\n" + str(predecessors))
    return distances, predecessors


def get_trails(predecessors: Dict[int, int]) -> Dict[int, List[int]]:
    """
    Zwraca słownik z wszystkimi sciezkami do kazdego wierzcholka
    """
    trails = {}
    for vertex in predecessors.keys():
        trails[vertex] = get_trail_to_vertex(predecessors, vertex)
    return trails


def get_trail_to_vertex(predecessors: Dict[int, int], vertex: int) -> List[int]:
    """
    Zwraca sciezke do danego wierzcholka
    """
    if predecessors[vertex] is None:  # przejscie z tego samego wierzcholka do tego samego
        return [vertex]
    return get_trail_to_vertex(predecessors, predecessors[vertex]) + [vertex]


def main():
    g = create_rand_consistent_weighted_graph(10, 1, 10)
    draw(g, "spojny_losowy_graf_wazony.png")

    print("\nZestaw 3, zadanie 2 - Dijkstra:")
    start_vertex = 3
    distances, predecessors = dijkstra(g, start_vertex)
    trails = get_trails(predecessors)
    print('START: s = ' + str(start_vertex))
    for vertex, trail in zip(distances.keys(), trails.keys()):
        print(f"d({vertex}) = {distances[vertex]} ==> {trails[trail]}")


if __name__ == "__main__":
    main()
