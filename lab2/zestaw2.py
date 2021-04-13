import collections
import random

# Funkcja pomocnicza z zestawu 1
def from_matrix_neighbour_to_list(matrix):
    list = {}

    i = 0
    for row in matrix:
        i += 1
        row_list = []
        lenght = len(row)
        for j in range(lenght):
            if row[j] == 1:
                row_list.append(j + 1)
        list[i] = row_list
    return list
	
# Proste sortowanie (może nie trzeba było tego pisać, ale nie znam się na tym języku)    
# Na wejściu przyjmuje ciąg graficzny
# Zwraca posortowany ciąg graficzny
def bubble_sort(arr):
    temp = 0
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
	
# Funkcja sprawdza czy w sekwencji jest nieparzysta liczba elementów nieparzystych
# Na wejściu przyjmuje ciąg graficzny
# Zwraca true jeżeli przekazany ciąg jest ciągiem graficznym, w przeciwnym wypadku false
def calculate_odd_elements(arr):
    counter = 0;
    isDegreeSeq = True;
    for i in range(0, len(arr)):
        if arr[i] % 2 == 1:
            counter = counter + 1
    if counter % 2 == 1:
        isDegreeSeq = False
    return isDegreeSeq
	
# Algorytm sprawdzający czy sekwencja liczb jest ciągiem graficznym
# Na wejściu przyjmuje ciąg graficzny
# Zwraca true jeżeli przekazany ciąg jest ciągiem graficznym, w przeciwnym wypadku false
def degree_seq(arr):
    # Jeżeli ilość nieparzystych stopni jest nieparzysta to wiadomo że sekwencja nie jest ciągiem graficznym
    if calculate_odd_elements(arr):
        # Sortowanie tablicy
        arr = bubble_sort(arr)
        while True:
            # Jeżeli wszystkie elementy sekwencji zostały wyzerowane to jest to ciąg graficzny
            allZeros = all(elem == 0 for elem in arr)
            if allZeros == True:
                return allZeros
            # Sprawdzenie czy po aktualizacji sekwencji nie występuje w niej liczba ujemna
            isNegative = False
            for i in range(1, len(arr)):
                if arr[i] < 0:
                    isNegative = True
            # Jeżeli jedna z liczb w sekwencji jest ujemna lub wartość jednej z liczb jest większa od długości sekwencji zwracany jest false
            if arr[0] < 0 or arr[0] >= len(arr) or isNegative:
                return False
            # Aktualizacja sekwencji poprzez zmniejszenie odpowiednich liczb
            for i in range(1, arr[0]+1):
                arr[i] = arr[i] - 1
            arr[0] = 0
            # Posortowanie zaktualizowanej sekwencji
            arr = bubble_sort(arr)
    else:
        return False
		
# Wyznaczenie sumy tablicy jednowymiarowej macierzy
# Funkcja jest używana to obliczania stopni wierzchołków dla macierzy sąsiedztwa
# Przyjmuje rząd z macierzy sąsiedztwa
# Zwraca sumę która jest stopniem wierzchołka
def sum(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    return sum
	
# Sprawdzenie czy wierzchołki w macierzy sąsiedztwa mają stopnie zgodne z wymaganymi
# Przyjmuje macierz sąsiedztwa oraz ciąg graficzny
# Zwraca tablicę zawierającą indeksy wierzchołków o błędnych stopniach
def check_matrix_correctness(matrix, degrees):
    errorsArr = []
    tmp = 0
    for i in range(len(matrix)):
        tmp = sum(matrix[i])
        if tmp != degrees[i]:
            errorsArr.append(i)
    return errorsArr

# Funkcja tworząca graf k-regularny
# Przyjmuje k - stopień pojedyńczego wierzchołka, numOfVertices - liczbę wierzchołków
# Zwraca macierz lub -1 jeśli nie można utworzyć macierzy
def generate_k_regular_graph(k, numOfVertices):
    # Inicjalizacja pustej tablicy do przechowywania stopni wierzchołków
    arr = []
    # Przypisanie do tablicy odpowiednich stopni wierzchołków
    for i in range(numOfVertices):
        arr.append(k)
    # Skopiowanie tablicy
    copy = arr.copy()
    # Inicjalizacja macierzy reprezentującej graf
    matrix = [[0 for i in range(len(copy))] for j in range(len(copy))]
    # Inicjalizacja licznika
    counter = 0
    # Inicjalizacja kroku
    step = 1
    # Inicjalizacja iteratora przechodzącego po wartościach ciągu graficznego 
    idx = 0
    # Sprawdzenie czy ciąg jest ciągiem graficznym
    if degree_seq(arr):
        # W każdym kroku przechodzi po kolejnym wierzchołku tworzonej macierzy 
        for step in range(0, len(copy)):
            # Sprawdzenie ile krawędzi wychodzi z aktualnie odwiedzanego wierzchołka 
            counter = sum(matrix[step])
            # Nowe krawędzie dodawane są od obecnego wierzchołka do "większych" wartością wierzchołków, aby nie zmieniać stopnia już odwiedzonych wierzchołków
            for i in range(step+1, len(copy)):
                    # Jeżeli stopień aktualnie odwiedzanego wierzchołka na to pozwala, to tworzy się nową krawędź
                    if sum(matrix[i]) < copy[i]:
                        # Sprawdzenie stopnia drugiego wierzchołka nowo utworzonej krawędzi
                        if counter < copy[idx]:
                            matrix[step][i] = 1
                            matrix[i][step] = 1
                            # Inkrementacja stopnia obenie odwiedzanej krawędzi
                            counter = counter + 1        
            # Przejście do kolejnego wierzchołka w ciągu graficznym
            idx = idx + 1
        #Zmienna pomocnicza określająca czy została zmieniona krawędź
        changed = False
        # Tablica przechowująca indeksy wierzchołków, które mają nieprawidłowe stopnie
        errors = check_matrix_correctness(matrix, copy)
        # Dopóki występują wierzchołki, które mają złe ilości krawędzi z nich wychodzących
        while not len(errors) == 0:
            # Dla każdego elementu w tablicy błędnych wierzchołków
            for elem in errors:
                changed = False
                for j in range(len(matrix)): 
                    if j != elem and matrix[elem][j] == 0: #wyznaczanie nowej krawędzi, brane jest jakiekolwiek 0 spoza przekątnej
                         for k in range(len(matrix[j])): #szukanie krawędzi, czyli matrix[j][k] == matrix[k][j] == 1
                            if k != elem and matrix[j][k] == 1: #jeżeli algorytm znajdzie taką krawędź, to usuwamy ją ze względu na zachowanie stopnia wierzchołków j i k
                                #print("j = " + str(j) + " k = " + str(k) + " elem = " + str(elem))
                                # Usunięcie starej krawędzi i utworzenie dwóch nowych krawędzi
                                matrix[j][k] = 0
                                matrix[k][j] = 0
                                matrix[elem][j] = 1
                                matrix[j][elem] = 1
                                matrix[k][elem] = 1
                                matrix[elem][k] = 1
                                # Informacja, że dla danego wierzchołka zaszła zmiana
                                changed = True
                            # Jedna zmiana wystarczy, trzeba sprawdzić rezultaty
                            if changed:
                                break
                    # Jedna zmiana wystarczy, trzeba sprawdzić rezultaty
                    if changed:
                        break
            # Ponowne sprawdzenie czy po zmianie wszystkie wierzchołki mają właściwe ilości krawędzi wychodzących
            errors = check_matrix_correctness(matrix, copy)
        return matrix
    else:
        return -1
	
# Funckja tworzy graf zbudowany na podstawie zadanego ciągu graficznego
# Przyjmuje ciąg graficzny
# Zwraca utworzony graf lub -1 jeżeli grafu nie da się utworzyć na podstawie zadanego ciągu
def create_graph_from_seq(arr):
    # Kopia tablicy przechowującej stopnie wierzchołków
    copy = arr.copy();
    # Zmienna pomocnicza do określenia, czy ciąg graficzny nie jest grafem k-regularnym
    isSame = True
    # Sprawdzenie czy graf jest k-regularny
    for i in range(len(arr)):
        if arr[i] != arr[0]:
            isSame = False
    # Jeżeli graf jest k-regularny wywoływana jest funkcja dedykowana grafom k-regularnym
    if isSame:
        matrix = generate_k_regular_graph(arr[0], len(arr))
        return matrix
    # Słownik potrzebny do przechowywania informacji o wierzchołkach izolowanych
    zeros = {}
    zeros[0] = []
    # Uzupełnienie słownika o wierzchołki izolowane
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros[arr[i]].append(i)
    # Inicjalizacja macierzy reprezentującej graf
    matrix = [[0 for i in range(len(copy))] for j in range(len(copy))]
    # Inicjalizacja licznika 
    counter = 0
    # Inicjalizacja kroku
    step = 1
    # Inicjalizacja iteratora przechodzącego po wartościach ciągu graficznego
    idx = 0
    # Sortowanie stopni wierzchołków
    copy = bubble_sort(copy)
    # Jeżeli ciąg jest ciągiem graficznym to tworzona jest macierz, w przeciwnym wypadku funkcja zwraca -1
    if degree_seq(arr):
        # W każdym kroku przechodzi po kolejnym wierzchołku tworzonej macierzy
        for step in range(0, len(copy)):
            # Sprawdzenie ile krawędzi wychodzi z aktualnie odwiedzanego wierzchołka
            counter = sum(matrix[step])
            # Nowe krawędzie mogą być dodane tylko od obecnego wierzchołka do wierzchołków o "większych" wartościach
            for i in range(step+1, len(copy)):
                # Upewnienie się, że nie jest to wierzchołek izolowany
                if not i in zeros[0] and not step in zeros[0]:
                    # Sprawdzenie czy stopień wierzchołka na drugim końcu krawędzi nie zostanie przekroczony
                    if sum(matrix[i]) < copy[i]:
                        # Utworzenie krawędzi
                        if counter < copy[idx]:
                            matrix[step][i] = 1
                            matrix[i][step] = 1
                            # Inkrementacja obecnie odwiedzanego stopnia wierzchołka
                            counter = counter + 1        
            # Przejście do kolejnego wierzchołka w ciągu graficznym
            idx = idx + 1
        return matrix
    else:
        return -1
		
# Funkcja randomizująca graf
# Przyjmuje graph - graf zadany macierzą sąsiedztwa, number - ilość randomizacji
# Funkcja nic nie zwraca
def randomize(graph, number):
    # Randomizacja jest wykonywana określoną liczbę razy
    for rands in range(number):
        # Zmienna pomocnicza służąca do określenia liczby iteracji, jeżeli dopuszczalna liczba iteracji zostanie przekroczona randomizacja zostanie zakończona
        i = 0
        # Zmienna pomocnicza potrzebna do losowania liczb
        size = len(graph)-1
        # Losowanie wierzchołków pierwszej krawędzi
        firstIdx = random.randint(0, size)
        secondIdx = random.randint(0, size)
        # Dostosowywanie wierzchołków pierwszej krawędzi
        # Jeżeli nie można dostosować wierzchołków program zostanie przerwany przez przekroczenie liczby dopuszczalnych iteracji
        while graph[firstIdx][secondIdx] != 1:
            firstIdx = random.randint(0, size)
            i = 0
            while firstIdx == secondIdx:
                secondIdx = random.randint(0, size)
                i = i + 1
                if i == 100:
                    break
            if i == 100:
                break
        if i == 100:
            print("Couldn't randomize graph!")
            return
        i = 0
        # Losowanie wierzchołków drugiej krawędzi
        thirdIdx = random.randint(0, size)
        fourthIdx = random.randint(0, size)
        # Dostosowanie wierzchołków drugiej krawędzi
        while thirdIdx == firstIdx or thirdIdx == secondIdx or graph[thirdIdx][fourthIdx] != 1:
            thirdIdx = random.randint(0, size)
            while thirdIdx == fourthIdx or fourthIdx == firstIdx:
                fourthIdx = random.randint(0, size)
                i = i + 1
                if i == 100:
                    break
            if i == 100:
                break
        if i == 100:
            print("Couldn't randomize graph!")
            return
        #print("firstIdx = " + str(firstIdx) + " secondIdx = " + str(secondIdx) + " thirdIdx = " + str(thirdIdx) + " fourthIdx = " + str(fourthIdx))
        # Warunki porównujące indeksy nie dopuszczają do sytuacji zapisania 1 na diagonali, pozostałe warunki sprawdzają czy nie ma krawędzi w miejscach gdzie miała powstać nowa krawędź
        if firstIdx != fourthIdx and firstIdx != secondIdx and thirdIdx != fourthIdx and secondIdx != thirdIdx and graph[firstIdx][fourthIdx] == 0 and graph[secondIdx][thirdIdx] == 0:
            graph[firstIdx][secondIdx] = 0
            graph[secondIdx][firstIdx] = 0
            graph[firstIdx][fourthIdx] = 1
            graph[fourthIdx][firstIdx] = 1
            graph[thirdIdx][fourthIdx] = 0
            graph[fourthIdx][thirdIdx] = 0
            graph[secondIdx][thirdIdx] = 1
            graph[thirdIdx][secondIdx] = 1
			
# Funkcja przeszukująca graf w głąb
# Przyjmuje numer iteracji, wierzchołek, macierz sąsiedztwa i stos reprezentowany przez tablicę
# Funkcja nic nie zwraca
def components_r(nr, v, graph, comp):
    for j in range(len(graph.get(v))):
        # Jeżeli jakiś wierzchołek nie był wcześniej odwiedzony to następuje przepisanie wartości z wierzchołka z którego przyszliśmy
        if comp[graph.get(v)[j]-1] == -1:
            comp[graph.get(v)[j]-1] = nr
            components_r(nr, graph.get(v)[j], graph, comp)
			
# Funkcja wyznaczająca spójne składowe
# Przyjmuje graf w postaci macierzy sąsiedztwa
# Funkcja nic nie zwraca
def components(graph):
    # Zmienna oznaczająca nr spójnej składowej
    nr = 0
    # Tablica oznaczająca wszystkie wierzchołki jako nieodwiedzone
    comp = [-1 for i in range(len(graph))]
    for i in range(len(graph)):
        # Jeżeli wierzchołek jest nieodwiedzony to inkrementujemy jego wartość
        if comp[i] == -1:
            nr = nr + 1
            # Przypisanie ilości odwiedzeń danego wierzchołka
            comp[i] = nr
            # Przeszukiwanie w głąb dla danego wierzchołka
            components_r(nr, i+1, graph, comp)
    # Licznik odwiedzeń
    counter = 0
    # Słownik, w którym do ilości odwiedzeń przypisywany jest indeks wierzchołka
    dicto = {}
    # Utworzenie kluczy w słowniku, wartości są aktualnie pustymi tablicami
    for i in range(len(comp)):
        if comp[i] != counter:
            counter = comp[i]
            dicto[counter] = []
    # Uzupełnienie tablic w słowniku
    for i in range(len(comp)):
        dicto[comp[i]].append(i+1)
    # Sortowanie kluczy słownika
    sorted_dict = collections.OrderedDict(sorted(dicto.items()))
    # Wypisanie posortowanego słownika
    temp = ""
    for i in range(1, len(sorted_dict)+1):
        temp = temp + str(i) + ") "
        for elem in sorted_dict[i]:
            temp = temp + str(elem) + " "
        print(temp)
        temp = ""
    # Wyszukanie najdłuższej ścieżki poprzez sprawdzanie długości tablic dla poszczególnych odwiedzeń
    longest = -1
    longest_dict_idx = 0
    for i in range(1, len(sorted_dict)+1):
        if len(sorted_dict[i]) > longest:
            longest = len(sorted_dict[i])
            longest_dict_idx = i
    # Sformatowane wypisanie rezultatu
    print("Najwieksza skladowa ma numer " + str(longest_dict_idx) + ".")
	
# Funkcje wyznaczająca cykl Eulera
# Funkcja przyjmuje stos reprezentowany przez tablicę, który służy do przechowywania numerów wierzchołków, indeks reprezentujący wierzchołek, macierz będącą grafem
def find_euler_cycle(cycle, idx, graph):
    # Przejście po wszystkich krawędziach wychodzących z wierzchołka idx
    for j in range(len(graph[idx])):
        # Jeżeli jest krawędź to ją wymazuje
        if graph[idx][j] != 0:
            graph[idx][j] = 0
            graph[j][idx] = 0
            # Rekurencyjne wywołanie funkcji dla wierzchołka na drugim końcu krawędzi
            find_euler_cycle(cycle, j, graph)
    # Wrzucenie na stos wierzchołka po wymazaniu wszystkich krawędzi wychodzących z niego
    cycle.append(idx+1)
	
# Funkcja zwracająca losowy ciąg graficzny o zadanej długości
# Funkcja przyjmuję liczbę wyznaczającą ilość wierzchołków tworzonego grafu
def prepare_random_vertices(numberOfVertices):
    # Inicjalizacja tablicy wierzchołków wartościami -1
    vertices = [-1 for i in range(numberOfVertices)]
    # Dla każdego indeksu losowana jest liczba reprezentująca stopień wierzchołka
    for i in range(numberOfVertices):
        randNum = random.randint(1, numberOfVertices)
        while (randNum % 2 != 0 or randNum == numberOfVertices):
            randNum = random.randint(1, numberOfVertices)
        vertices[i] = randNum
    return vertices
	
# Funkcja tworząca losowy graf eulerowski
# Funkcja nic nie zwraca
def generate_euler_graph(numberOfVertices):
    # Jeżeli graf jest zbudowany z mniej niż 3 wierzchołków to nie można utworzyć cyklu Eulera
    if numberOfVertices < 3:
        print(" ")
        return
    # Losowanie ciągu graficznego o zadanej długości
    vertices = prepare_random_vertices(numberOfVertices)
    # Utworzenie grafu na podstawie wylosowanego ciągu graficznego
    graph = create_graph_from_seq(vertices)
    # Jeżeli graf został utworzony to go wypisujemy w formie listy
    if graph != -1:
        print(from_matrix_neighbour_to_list(graph))
    # Jeżeli graf nie został za pierwszym razem utworzony to algorytm próbuje do skutku    
    while graph == -1:
        vertices = prepare_random_vertices(numberOfVertices)
        graph = create_graph_from_seq(vertices)
        if graph != -1:
            print(from_matrix_neighbour_to_list(graph))
    # Inicjalizacja tablicy przechowującej ścieżkę Eulera
    cycle = []
    # Wyznaczenie ścieżki Eulera dla wylosowanego grafu
    find_euler_cycle(cycle, 0, graph)
    # Inicjalizacja stringa do sformatowanego wypisania ścieżki
    path = ""
    # Kolejne elementy ścieżki wypisujemy wg. sugerowanego formatu
    for i in range(len(cycle)):
        if i == 0:
            path = path + str(cycle[i])
        else:
            path = path + " - " + str(cycle[i])
    # Wypisanie ścieżki Eulera
    print(path)