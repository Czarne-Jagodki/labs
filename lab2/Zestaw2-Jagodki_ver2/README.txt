0. Zmiany względem ver1

a) Uwaga: mierzenie czasu w pythonie nieco mija się z celem...
Poprawki: Skoro przedstawione mierzenie czasów nie spełniało swojej funkcji, zostało ono usunięte.
		  Aktualnie zestaw nie wymaga modułu time.

b) Uwaga: Błąd dla nieprawidłowych n-k jest nieco mylący.
Poprawki: Nastąpiła lekka modyfikacja metody def generate_k_regular_graph(k, numOfVertices).
		  Jeżeli wygenerowana tablica zawierająca stopnie wierzchołków nie jest sekwencją graficzną 
		  metoda rzuca wyjątek Exception o treści "It's not a degree sequence!". Jeżeli wygenerowana 
		  tablica jest sekwencją graficzną działanie funkcji nie uległo zmianie.

c) Uwaga: Funkcja randomizująca nie działa prawidłowo...
Poprawki: Metoda def randomize(graph, number) została napisana od nowa. Obecnie jej działanie polega
		  na wylosowaniu wierzchołka A, który jest niezerowego stopnia. Następnie spośród wierzchołków 
		  połączonych z wierzchołkiem A losowany jest wierzchołek B. W dalszej kolejności spośród 
		  wierzchołków, które nie są połączone z wierzchołkiem B losowany jest wierzchołek C. Na koniec
		  spośród wierzchołków połączonych z C i różnych od A losowany jest wierzchołek D.
		  Wszystkie warunki, które miała spełniać randomizacja zostały zachowane.
		  Jeżeli nie uda się znaleźć czterech wierzchołków, które spełniają te założenia (1000 prób),
		  to wypisany zostaje komunikat "Couldn't randomize the graph!". Najlepiej to sprawdzić dla 
		  grafów pełnych. 

d) Pozostałe zmiany:
- Dopisanie metody def check_all_zeros(graph, idx) jako funkcji pomocniczej dla randomize.
- def create_graph_from_seq(arr) rzuca wyjątek jeżeli nie może utworzyć grafu na podstawie przekazanej
  sekwencji (przekazana sekwencja nie jest sekwencją graficzną)

1. Wymagane moduły
Projekt do poprawnego działania wymaga zaimportowania następujących modułów:
- networkx
- matplotlib.pyplot
- numpy
- math
- collections
- random

2. Sposób użycia
W zamyśle kod projektu był przeznaczony do używania w środowisku Jupyter Notebook. Definicje
funkcji zostały skopiowane do pliku src/zestaw2.py, jednak kod nie został przetestowany w warunkach 
konsolowych.