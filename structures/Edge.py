from labs.structures.Vertex import Vertex


class Edge:
    """
    Klasa reprezentujaca krawedz
    """
    vertices: tuple
    weight: int
    visited: bool

    def __init__(self, first_vertex: Vertex, second_vertex: Vertex, weight: int = 1, visited: bool = False) -> None:
        self.vertices = (first_vertex, second_vertex)
        self.visited = visited
        self.weight = weight

    def get_vertices_ids(self) -> tuple:
        return self.vertices

    def get_weight(self):
        return self.weight
