from typing import List, Set
from Edge import Edge
from Vertex import Vertex


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
                # self.vertices.add(edge[0])
                # self.vertices.add(edge[1])

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

    def get_vertices_lvls(self) -> List[int]:
        """
        Zwraca liste stopni wierzcholkow
        """
        nr_of_vertices = len(self.get_vertices())
        vertex_level = [0] * nr_of_vertices
        edges = self.get_edges()
        for edge in edges:
            edge_vertices = edge.get_vertices_ids()
            # zwiekszamy stopien danego wierzcholka o jeden dla kazdej krawedzi
            # i zapisujemy inkrementowana wartosc stopnia wierzcholka pod danym id wierzcholka w tablicy
            vertex_level[edge_vertices[0].get_id()] += 1
            vertex_level[edge_vertices[1].get_id()] += 1
        return vertex_level

    def is_consistent(self) -> bool:
        """
        Sprawdza czy graf jest spojny
        :return: prawda/falsz
        """
        vertices_lvls = self.get_vertices_lvls()
        nr_of_zero_lvls = len(list(filter(lambda lvl: lvl == 0, vertices_lvls)))
        # jesli istnieje wierzcholek ktorego stopien == 0, to graf na pewno nie jest spojny
        return nr_of_zero_lvls == 0

    def is_weighted(self) -> bool:
        """
        Zwraca informacje czy krawedzie grafu maja wagi
        :return: prawda/falsz
        """
        return self.weighted
