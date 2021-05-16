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
    size = len(neigh_matrix)
    for i in range(size):
        for j in range(size):
            if neigh_matrix[i][j] == 1:
                tmp = random.randint(min, max)
                while tmp == 0:
                    tmp = random.randint(min, max)
                neigh_matrix[i][j] = tmp
    return neigh_matrix


def bellman_ford_algorithm(G, src):
    connections = []
    for u in range(len(G)):
        for v in range(len(G[0])):
            if G[u][v] != 0:
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

n = 5
p = 0.5
test_digraph = generate_random_strongly_coherent_digraph(n, p)
print(test_digraph)
matrix_with_weights = add_randomized_weights_to_digraph(test_digraph, -3, 5)
print(matrix_with_weights)

# digraph = [
#     [0, -1, -4],
#     [4, 0, 0],
#     [0, 2, 0]
# ]

# digraph = [
#     [0, 6, 3, 0, -1, 0, 0],
#     [10, 0, -5, -4, 4, 0, 4],
#     [0, 0, 0, 0, 0, 2, 0],
#     [0, 5, 0, 0, 0, 0, 9],
#     [0, 0, 0, 0, 0, 0, -4],
#     [0, 9, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 4, 0]
# ]
#
# for i in range(len(digraph)):
#     bellman_ford_algorithm(digraph, i)

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
            if (is_included_in_spt[vertex] == False) and (distance[vertex] > (distance[cur_vert] + modifiedG[cur_vert][vertex])) and (G[cur_vert][vertex] != 0):
                distance[vertex] = distance[cur_vert] + modifiedG[cur_vert][vertex]

    print("w\t\tdist")
    for i in range(vertices):
        print("%d\t\t%d" % (i, distance[i]))


digraph = [
    [0, 6, 3, 0, -1, 0, 0],
    [10, 0, -5, -4, 4, 0, 4],
    [0, 0, 0, 0, 0, 2, 0],
    [0, 5, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, -4],
    [0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0]
]

# ex3:
bell_digraph = []
for i in range(len(digraph)):
    bell_digraph.append(bellman_ford_algorithm(digraph, i))
# macierz najkrótszych ścieżek, element w wierszu w i kolumnie k oznacza długość najkrótszej ścieżki od wierzchołka w do k
print(bell_digraph)

#
# def johnson_algorithm(G):
#     return
