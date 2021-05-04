import pickle
from typing import List, Set
from .Edge import Edge
from .Vertex import Vertex


class Graph:
    """
       Klasa reprezentujaca Graf
    """
    edges: List[Edge]
    vertices: Set[Vertex]
    weighted: bool

    def __init__(self, edges: List[Edge] = None, vertices: Set[Vertex] = None, weighted=False):
        """
        Inicjalizacja grafu
        :param edges: krawedzie
        :param vertices: wezly
        :param weighted: czy krawedzie maja wagi
        """
        if edges is None:
            edges = []
        if vertices is None:
            vertices = set()
        self.edges = edges
        self.vertices = vertices
        self.weighted = weighted

    def add_vertex(self, vertex: Vertex):
        """
        Dodaje nowy wezel
        :param vertex: wezel
        """
        self.vertices.add(vertex)

    def add_edges(self, edges: Set[tuple]):
        """
        Dodaje krawedzie
        :param edges: zbior tupli wierzcholkow lub wierzcholkow i wagi
        """
        for edge in edges:
            # tutaj dodajemy krawedzie do grafu
            has_edge = None
            for x in self.edges:
                # jesli krawedz juz zostala dodana do grafu to wychodzimy z wewnetrznej petli i
                # sprawdzamy kolejna krawedz ze zbioru krawedzi ktore chcemy dodac
                if (x.get_vertices_ids()[0] == edge[1] and x.get_vertices_ids()[1] == edge[0]) or (
                        x.get_vertices_ids()[0] == edge[0] and x.get_vertices_ids()[1] == edge[1]):
                    has_edge = x
                    break
            # jesli nie to dodajemy brakujaca krawedz
            if has_edge is None:
                if self.weighted:
                    self.edges.append(Edge(edge[0], edge[1], edge[2]))
                else:
                    self.edges.append(Edge(edge[0], edge[1]))

    def get_edges(self) -> List[Edge]:
        """
        Zwraca liste krawedzi
        """
        return self.edges

    def get_vertices(self) -> Set[Vertex]:
        """
        Zwraca zbior wezlow
        """
        return self.vertices

    # def get_vertices_lvls(self) -> List[int]:
    #     """
    #     Zwraca liste stopni wierzcholkow
    #     """
    #     nr_of_vertices = len(self.get_vertices())
    #     vertex_level = [0] * nr_of_vertices
    #     edges = self.get_edges()
    #     for edge in edges:
    #         edge_vertices = edge.get_vertices_ids()
    #         # zwiekszamy stopien danego wierzcholka o jeden dla kazdej krawedzi
    #         # i zapisujemy inkrementowana wartosc stopnia wierzcholka pod danym id wierzcholka w tablicy
    #         vertex_level[edge_vertices[0].get_id()] += 1
    #         vertex_level[edge_vertices[1].get_id()] += 1
    #     return vertex_level

    def dfs(self, temp: List[int], v: int, visited: List[bool]) -> List[int]:
        """
        Algorytm przeszukiwania w glab
        :return: lista wierzcholkow tworzacych spojna skladowa
        """
        # ustaw obecny wierzcholek na odwiedzony
        visited[v] = True

        # dodaj wierzcholek do listy
        temp.append(v)

        # znajdujemy sasiadow wierzcholka v
        list_of_neigbours = self.find_neighbours(v)

        # powtorz dla kazdego wierzcholka bedacego sasiadem v ktorego jeszcze nie odwiedzilismy
        for i in list_of_neigbours:
            if not visited[i]:
                # zaktualizuj liste
                temp = self.dfs(temp, i, visited)
        return temp

    def connected_components(self) -> List[List[int]]:
        """
        Zwraca liste spojnych skladowych
        """
        visited = [False] * len(self.get_vertices())
        components = []
        for v in range(len(self.get_vertices())):
            if not visited[v]:
                temp = []
                components.append(self.dfs(temp, v, visited))
        return components

    def is_consistent(self) -> bool:
        """
        Sprawdza czy graf jest spojny
        :return: prawda/falsz
        """
        # jezeli graf ma jedna spojna skladowa -> jest spojny
        return len(self.connected_components()) == 1

    def is_weighted(self) -> bool:
        """
        Zwraca informacje czy krawedzie grafu maja wagi
        :return: prawda/falsz
        """
        return self.weighted

    def find_neighbours(self, vertex_id) -> List[int]:
        """
        Znajduje sasiadow danego wierzcholka w zadanym grafie
        :param vertex_id: id wierzcholka, dla ktorego znajdujemy sasiadow
        :param graph: zadany graf
        :return: lista sasiadow
        """
        neighbours = []
        edges = self.get_edges()
        for edge in edges:
            tuple_of_vertices = edge.get_vertices_ids()
            # jezeli wierzcholek obecny w krawedzi, drugi wierzcholek jest jego sasiadem
            if tuple_of_vertices[0].get_id() == vertex_id:
                neighbours.append(tuple_of_vertices[1].get_id())
                continue
            # analogicznie
            if tuple_of_vertices[1].get_id() == vertex_id:
                neighbours.append(tuple_of_vertices[0].get_id())
                continue
        return neighbours

    def find_edge(self, first_vertex: int, second_vertex: int) -> Edge:
        """
        Znajduje i zwraca krawedz dwoch wierzcholkow
        """
        for edge in self.get_edges():
            vertices = edge.get_vertices_ids()
            vertex_1 = vertices[0].get_id()
            vertex_2 = vertices[1].get_id()
            if (vertex_1 == first_vertex and vertex_2 == second_vertex) or (
                    vertex_1 == second_vertex and vertex_2 == first_vertex):
                return edge

    def save_to_file(self, filename: str = 'graph.txt') -> None:
        file = open(filename, 'wb')
        pickle.dump(self, file)
        file.close()


def load_from_file(filename: str) -> Graph:
    file = open(filename, 'rb')
    return pickle.load(file)
