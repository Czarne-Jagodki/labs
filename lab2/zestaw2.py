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

# Funkcja naprawiająca macierze, które mają nieprawidłowe stopnie wierzchołków
# Przyjmuje jako argument macierz sąsiedztwa reprezentującą graf oraz ciąg graficzny
# Funkcja działa tylko na przekazanej do niej macierzy - nic nie zwraca
def repair_matrix(matrix, copy):
    # Sprawdzenie czy są wierzchołki o błędnych stopniach
    errors = check_matrix_correctness(matrix, copy)
    while not len(errors) == 0:
        # To jest specjalny przypadek dla macierzy o stopniach np. [2, 2, 2, 2, 2]
        # W powyższym przypadku kod w else się zapętla (nie umiem tego wytłumaczyć)
        if len(errors) % 2 == 0 and sum(matrix[errors[0]]) != sum(matrix[errors[1]]):
                firstIdx = -1
                secondIdx = -1
                if sum(matrix[errors[0]]) > sum(matrix[errors[1]]):
                    firstIdx = errors[0]
                    secondIdx = errors[1]
                else:
                    firstIdx = errors[1]
                    secondIdx = errors[0]
                #print("firstIdx = " + str(firstIdx) + " secondIdx = " + str(secondIdx))
                for j in range(len(matrix)):
                    if matrix[firstIdx][j] == 1 and matrix[j][secondIdx] == 0:
                        matrix[firstIdx][j] = 0
                        matrix[j][firstIdx] = 0
                        matrix[j][secondIdx] = 1
                        matrix[secondIdx][j] = 1
                        break;
                errors = check_matrix_correctness(matrix, copy)
        else: # Dla większości macierzy
            # Algorytm naprawia pojedyńczo każdy wierzchołek
            for elem in errors:
                # Ustawiamy flagę oznaczającą modyfikację wierzchołka
                changed = False
                # Losowanie indeksów
                # Losowanie występuje z tego powodu, że w niektórych przypadkach
                # iteracyjne przechodzenie for'em po wierzchołkach powodowało zapętlenie
                # tzn nie zgadzały się na zmianę wierzchołki 1 i 2
                firstIdx = random.randint(0, len(matrix)-1)
                secondIdx = random.randint(0, len(matrix)-1)
                # Iter jest pewnego rodzaju 'bezpiecznikiem'. Jeżeli nie można znaleźć odpowiednich
                # wierzchołków do zamiany to opuszczamy funkcje
                iter = 0
                while firstIdx in errors or secondIdx in errors or firstIdx == secondIdx or sum(matrix[firstIdx]) != sum(matrix[secondIdx]) or matrix[firstIdx][secondIdx] != 1:
                    iter = iter + 1
                    firstIdx = random.randint(0, len(matrix)-1)
                    secondIdx = random.randint(0, len(matrix)-1)
                    if iter == 1000:
                        break
                if iter == 1000:
                    print("Couldn't repair matrix!")
                    break
                #print("firstIdx = " + str(firstIdx) + " secondIdx = " + str(secondIdx)) 
                # Sprawdzenie czy na pewno nie ma krawędzi łączącej wylosowane wierzchołki z błędnym
                if matrix[errors[0]][firstIdx] == 0 and matrix[errors[0]][secondIdx] == 0:
                    # Zamiana odbywa się w taki sposób, żeby zachować stopnie wylosowanych wierzchołków
                    # W związku z tym stopień 'błędnego' wierzchołka zwiększa się o 2 
                    matrix[firstIdx][secondIdx] = 0
                    matrix[secondIdx][firstIdx] = 0
                    matrix[firstIdx][errors[0]] = 1
                    matrix[errors[0]][firstIdx] = 1
                    matrix[secondIdx][errors[0]] = 1
                    matrix[errors[0]][secondIdx] = 1
                # Aktualizacja listy błędów
                errors = check_matrix_correctness(matrix, copy)
            if iter == 1000:
                # Formalnie można to zakomentować, ale wg mnie warto zobaczyć strukturę macierzy której nie można zmienić
                print(matrix)
                break
                #print(errors)

# Funckja tworzy graf zbudowany na podstawie zadanego ciągu graficznego
# Przyjmuje ciąg graficzny
# Zwraca utworzony graf lub -1 jeżeli grafu nie da się utworzyć na podstawie zadanego ciągu        
def create_graph_from_seq(arr):
    # Kopia tablicy przechowującej stopnie wierzchołków
    copy = arr.copy();
    # Słownik potrzebny do przechowywania informacji o wierzchołkach izolowanych
    zeros = {}
    zeros[0] = []
    # 0 na liście oznacza że występuje wierzchołek izolowanych
    # Zdarzają się przypadki, gdzie wystąpienie tego wierzchołka w środku listy wywalało program np. [3, 2, 0, 2, 3]
    # W związku z tym następuje sortowanie tablicy, żeby wierzchołek izolowany znalazł się na końcu i nie przeszkadzał
    if 0 in arr:
        arr = bubble_sort(arr)
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
        # Naprawa macierzy w przypadku występowania błędnych stopni wierzchołków
        repair_matrix(matrix, copy)
        return matrix
    else:
        return -1	

# Funkcja tworząca graf k-regularny
# Przyjmuje k - stopień pojedyńczego wierzchołka, numOfVertices - liczbę wierzchołków
# Zwraca macierz lub -1 jeśli nie można utworzyć macierzy
 def generate_k_regular_graph(k, numOfVertices):
    # Inicjalizacja pustej tablicy do przechowywania stopni wierzchołków
    arr = []
    # Przypisanie do tablicy odpowiednich stopni wierzchołków
    for i in range(numOfVertices):
        arr.append(k)
    # Zwraca funkcję tworzącą graf dla zadanego ciągu graficznego
    return create_graph_from_seq(arr)
		
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