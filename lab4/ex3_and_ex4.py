import kosaraju as kosoraju
import ex1 as ex1
import random as random

def check_if_is_strongly_coherent(list_matrix):
    kos = kosoraju.kosaraju(list_matrix)
    size = len(kos)
    for i in range(1, size+1):
        if kos[i] != 1:
            return False
    return True

def generate_random_strongly_coherent_digraph(n, p):
    matrix = ex1.rand_digraph_with_probability(n, p)
    list_matrix = ex1.from_matrix_neighbour_to_list(matrix)
    kosoraju.revert_matrix_values(list_matrix)

    while not check_if_is_strongly_coherent(list_matrix):
        matrix = ex1.rand_digraph_with_probability(n, p)
        list_matrix = ex1.from_matrix_neighbour_to_list(matrix)
        kosoraju.revert_matrix_values(list_matrix)

    return list_matrix


def from_list_to_neighbour_matrix(list):
    """
    Function converts neighbourhood list to neighbourhood matrix of digraph
    :param list: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    :return: matrix which represents neighbourhood matrix of digraph
    """
    matrix = []
    length = len(list)
    for elements in list.values():
        row = []
        for i in range(1, length + 1):
            if i in elements:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def add_randomized_weights_to_digraph(G, min, max):
    neigh_matrix = from_list_to_neighbour_matrix(G)
    weight_matrix = from_list_to_neighbour_matrix(G)
    size = len(neigh_matrix)
    for i in range(size):
        for j in range(size):
            if neigh_matrix[i][j] == 1:
                tmp = random.randint(min, max)
                # commented out, becouse we allow "0" as weight
                # while tmp == 0:
                #     tmp = random.randint(min, max)
                weight_matrix[i][j] = tmp
            else:
                weight_matrix[i][j] = None
    return neigh_matrix, weight_matrix


def bellman_ford_algorithm(G, src):
    connections = []
    for u in range(len(G)):
        for v in range(len(G[0])):
            if G[u][v] != None:
                connections.append([u, v, G[u][v]])

    vertices = len(G)
    edges = len(connections)

    distance = [float("Inf")] * vertices
    distance[src] = 0

    for i in range(vertices - 1):
        for j in range(edges):
            x = connections[j][0]
            y = connections[j][1]
            weight = connections[j][2]
            if distance[x] + weight < distance[y]:
                distance[y] = distance[x] + weight

    for i in range(edges):
        x = connections[i][0]
        y = connections[i][1]
        weight = connections[i][2]
        if distance[x] != float("Inf") and distance[x] + weight < distance[y]:
            print("Graf zawiera ujemny cykl!")
            return False

    # print("odleglosci wierzcholkow od zrodla:")
    # print("w\t\tdist")
    # for i in range(vertices):
    #     print("%d\t\t%d" % (i, distance[i]))

    return distance

#ex 3 part 1
# n = 5
# p = 0.5
# test_digraph = generate_random_strongly_coherent_digraph(n, p)
# print(test_digraph)
# neigh_matrix, weight_matrix = add_randomized_weights_to_digraph(test_digraph, -3, 5)
# print(neigh_matrix)
# print(weight_matrix)


from collections import defaultdict

def min_distance(distance, visited):
    (min, min_vert) = (float("Inf"), 0)
    for vertex in range(len(distance)):
        if min > distance[vertex] and visited[vertex] == False:
            (min, min_vert) = (distance[vertex], vertex)

    return min_vert

def dijkstra_algorithm(G, modifiedG, src):

    vertices = len(G)
    is_included_in_spt = defaultdict(int)
    distance = [float("Inf")] * vertices
    distance[src] = 0

    for _ in range(vertices):
        cur_vert = min_distance(distance, is_included_in_spt)
        is_included_in_spt[cur_vert] = True

        for vertex in range(vertices):
            if (is_included_in_spt[vertex] == False) and (distance[vertex] > (distance[cur_vert] + modifiedG[cur_vert][vertex])) and (G[cur_vert][vertex] != None):
                distance[vertex] = distance[cur_vert] + modifiedG[cur_vert][vertex]

    # print("w\t\tdist")
    # for i in range(vertices):
    #     print("%d\t\t%d" % (i, distance[i]))


digraph = [
    [None, -1, -4],
    [4, None, None],
    [None, 2, None]
]

# ex3:

def solve_bellman_ford(digraph):
    bell_digraph = []
    for i in range(len(digraph)):
        check = bellman_ford_algorithm(digraph, i)
        if check:
            bell_digraph.append(check)
        else:
            return False
    # macierz najkrótszych ścieżek, element w wierszu w i kolumnie k oznacza długość najkrótszej ścieżki od wierzchołka w do k
    return bell_digraph


def add_s(G):
    vertices = len(G)
    weight_matrix = []
    for i in range(vertices):
        weight_matrix.append([])
        for j in range(vertices):
            weight_matrix[i].append(G[i][j])
    for i in range(vertices):
        weight_matrix[i].append(None)
    additional_row = [0] * vertices
    additional_row.append(None)
    weight_matrix.append(additional_row)
    return weight_matrix


def johnson_algorithm(G):
    Gs = add_s(G)
    h = bellman_ford_algorithm(Gs, len(Gs)-1)
    if not h:
        print("ERR")
        return
    else:
        print(h)
        new_weights = []
        for i in range(len(Gs)):
            new_weights.append([])
            for j in range(len(Gs)):
                if Gs[i][j] != None:
                    new_weights[i].append(Gs[i][j] + h[i] - h[j])
                else:
                    new_weights[i].append(None)
        print(new_weights)

        D = []
        for i in range(len(G)):
            D.append([])
            for j in range(len(G)):
                D[i].append(new_weights[i][j])
        print(D)

        #tylko teraz dorzucić tu dijkstrę i powinno śmigać



johnson_algorithm(digraph)



