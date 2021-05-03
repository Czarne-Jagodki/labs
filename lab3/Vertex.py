class Vertex:
    """
    Klasa reprezentujaca wierzcholek
    """
    id: int
    visited: bool

    def __init__(self, given_id: int = None, visited: bool = False) -> None:
        """
        Inicjalizacja wierzcholka
        :param given_id: id wierzcholka czyli jego numer
        :param visited: czy odwiedzony
        """
        self.id = given_id
        self.visited = visited

    def __hash__(self) -> int:
        """
        <! Wymagane bo inaczej blad unhashable type !>
        Hashuje id wierzcholka
        :return: zwraca zhashowany numer (id) wierzcholka
        """
        return hash(self.id)

    def get_id(self) -> int:
        """
        Zwraca id wierzcholka (numer)
        :return: id wierzcholka
        """
        return self.id