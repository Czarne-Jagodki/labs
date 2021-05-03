from zad3 import create_distances_matrix
from typing import List
from zad1 import graph

'''
Funkcja wypisuje zadana macierz (liste wielu list) w estetycznej formie.
'''
def print_matrix(matrix: List[List]) -> None:
    for row in matrix:
        print(*row, sep='\t')

'''
Funkcja dla zadanego wierzcholka zwraca indeks minimalnej wartosci.
'''
def find_min_index(vector: List[int]) -> int:
    min_index = 0
    
    for i in range(1, len(vector)):
        if vector[i] < vector[min_index]:
            min_index = i
            
    return min_index

'''
Funkcja dla zadanej macierzy liczy sumy elementow w kazdym z wierszy i zwraca
je w postaci listy.
'''

def get_sum_vector(matrix: List[List]) -> list:
    sum_vector = list()
    
    for row in matrix:
        sum_vector.append(sum(row))
        
    return sum_vector

'''
Funkcja znajduje centrum grafu - dla zadanej macierzy odleglesci
dla calego grafu, funkcja zwraca indeks wierzcholksa, dla ktorego suma odleglosci
do wszystkich pozostalych wierzcholkow jest minimalna.
'''
def find_graph_center(distances_matrix: List[List]) -> int:
    sum_vector = get_sum_vector(distances_matrix) # pobieramy wektor sum kazdego z wierszy macierzy
    min_index = find_min_index(sum_vector) # odnajdujemy dla ktorego wierzcholka suma w wierszu jest najmniejsza
    
    return min_index

'''
Funkcja znajduje centrum minimax grafu - dla zadanej macierzy odleglosci
dla calego grafu, funkcja zwraca indeks wierzcholka, dla ktorego odleglosc
do najdalszego wierzcholka jest minimalna.
'''
def find_minimax_center(distances_matrix: List[List]) -> int:
    max_distances_vector = list()
    
    for row in distances_matrix:
        row.sort() # sortujemy rosnaco kazdy z wierszy w macierzy
        max_distances_vector.append(row[len(row) - 1]) # dodajemy najdalsze odleglosci do wektora
        
    min_index = find_min_index(max_distances_vector) # znajdujemy indeks minimalnej wartosci w wektorze
    
    return min_index
    

def main() -> None:
    distances_matrix = create_distances_matrix(graph)
    print_matrix(distances_matrix)
    graph_center = find_graph_center(distances_matrix)
    minimax_graph_center = find_minimax_center(distances_matrix)
    print(f'Centrum grafu to wierzcholek: {graph_center}')
    print(f'Centrum minimax grafu to wierzcholek: {minimax_graph_center}')

if __name__ == '__main__':
    main()
