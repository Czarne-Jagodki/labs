from itertools import combinations
from random import sample, randint
import matplotlib.pyplot as plt
import networkx as nx
from Github.structures.Graph import Graph
from Github.structures.Vertex import Vertex


def create_rand_consistent_weighted_graph(n: int = 5, weight_min: int = 1, weight_max: int = 10) -> Graph:
    """
    Funkcja tworzaca spojny graf losowy o zadanej liczbie wierczholkow i krawedziach o wadze pomiedzy
    weight_min a weight_max
    :param n: liczba wierzcholkow
    :param weight_min: waga min
    :param weight_max: waga max
    :return: gotowy graf
    """

    vertices = set([v for v in range(n)])  # zbior numerow wierzcholkow
    edges = set()  # zbior krawedzi (tupli o 3 polach) zlozonych z 2 wierczholkow i losowej wagi

    min_edges = n - 1  # minimalna liczba krawedzi
    max_edges = (n * (n - 1)) / 2  # maksymalna liczba krawedzi

    # losujemy liczbe krawedzi z przedzialu <min, max> (wlacznie)
    nr_of_edges = randint(min_edges, max_edges)
    counter = 1
    while True:
        # stworzenie wszystkich mozliwych 2-elementowych kombinacji wierzcholkow w postaci tupli
        vertex_comb = combinations(vertices, 2)

        # losowe wybranie kombinacji 2 wierzcholkow z listy vertex_comb, 'nr_of_edges' razy, czyli dla kazdej krawedzi
        rand_comb = sample(list(vertex_comb), nr_of_edges)

        # dodajemy do zbioru 'edges', tuple z wierzcholkami i waga
        for comb in rand_comb:
            edges.add((Vertex(comb[0]),
                       Vertex(comb[1]),
                       randint(weight_min, weight_max)))

        # tworzymy pusty graf wazony
        graph = Graph(weighted=True)

        # dodajemy wszystkie wierzcholki
        for vertex_id in vertices:
            graph.add_vertex(Vertex(vertex_id))

        # dodajemy krawedzie z naszych kombinacji
        graph.add_edges(edges)

        # powtarzamy proces dopoki graf nie bedzie spojny
        if graph.is_consistent():
            return graph


def draw(graph: Graph, filename: str = None):
    """
    Funkcja odpowiada za narysowanie grafu
    :param graph: graf do narysowania
    :param filename: opcjonalna nazwa pliku do zapisu w nim rysunku
    """
    # pusty graf
    nx_graph = nx.Graph()

    # dodanie wierzcholkow do grafu
    for vertex in graph.get_vertices():
        nx_graph.add_node(vertex.get_id())

    edges = graph.get_edges()

    # dodanie krawedzi do grafu
    for edge in edges:
        vertices_ids = edge.get_vertices_ids()
        if graph.is_weighted():
            nx_graph.add_edge(vertices_ids[0].get_id(), vertices_ids[1].get_id(), weight=edge.get_weight())
        else:
            nx_graph.add_edge(vertices_ids[0].get_id(), vertices_ids[1].get_id())

    # ustawienie numerow wierzcholkow
    labels = {}
    for i in range(len(graph.get_vertices())):
        labels[i] = i
    # pozycjonowanie na okregu
    pos = nx.circular_layout(nx_graph)

    # narysowanie grafu
    nx.draw(nx_graph, pos, labels=labels)

    # dodanie wag krawedzi do rysunku
    if graph.is_weighted():
        nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=nx.get_edge_attributes(nx_graph, "weight"))

    plt.axis("equal")  # symetrycznosc

    # ewentualny zapis do pliku
    if filename is not None:
        plt.savefig(filename, format="png")
    plt.show()

    # wyczyszczenie figury
    plt.clf()


def main():
    graph = create_rand_consistent_weighted_graph(5, 1, 10)
    draw(graph)


if __name__ == "__main__":
    main()
