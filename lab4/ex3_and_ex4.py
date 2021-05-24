import kosaraju as kosoraju
import ex1 as ex1
import random as random

def print_neigh_matrix_in_decent_way(G):
    """
    This function prints matrix that represents weights of edges in digraph in formatted,
    easy-to-read way and it replaces None with single dot (that means there is no connection
    betweet these two vertexes)
    can be also used to print shortest-paths matrix, althogh there is no None issue, it still can split rows
    into separated lines instead of printing it as extra long one line string
    :param G: matrix containing value of weights if there is connection from one to another vertex and None if there is not
    :return: this function returns nothing, just prints the matrix
    """
    def change_none_into_dot(el):
        if el == None:
            return '.'
        else:
            return str(el)

    print('[')
    for i in range(len(G)):
        line = '    ['
        for j in range(len(G)-1):
            line += change_none_into_dot(G[i][j]) + ', '
        line += change_none_into_dot(G[i][len(G)-1]) + ']'
        print(line)
    print(']')


def convert_to_neighbour_and_weight_matrix(G):
    """
    Tris function converts matrix containing weights between edges and None(if there is no connection between vertices)
    to two separate matrixes, first of them is neighbours matrix with 1 if there is edge from i to j vertex
    and 0 if there is not, and second of them with weights for those edges
    :param G: matrix containing value of weights if there is connection from one to another vertex and None if there is not
    :return: two matrixes, one being neighbour matrix and another one being weights matrix
    """
    neigh_matrix = []
    weight_matrix = []
    for i in len(G):
        for j in len(G):
            if G[i][j] != None:
                neigh_matrix[i].append[1]
                weight_matrix[i].append[G[i][j]]
            else:
                neigh_matrix[i].append[0]
                weight_matrix[i].append[0]
    return neigh_matrix, weight_matrix


def check_if_is_strongly_coherent(list_matrix):
    """
    Function checks whether graph is strongly coherent or not
    :param list_matrix: list of neighbours but reversed to the entry list
    :return: boolean - false if graph is not strongly coherent, true if it is
    """
    kos = kosoraju.kosaraju(list_matrix)
    size = len(kos)
    for i in range(1, size+1):
        if kos[i] != 1:
            return False
    return True


def generate_random_strongly_coherent_digraph(n, p):
    """
    Function generates randomized and strongly coherent digraph of given number of
    vertexes and given probability that there is an edge between two vertexes
    :param n: number of vertexes
    :param p: probability -> it is between [0,1]
    :return: it's a dictionary: keys are numbers of graph vertex and values
            are lists of other vertexes connected with them by edge
    """
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
    """
    This function only adds weights to all edges of digraph. The weights are generated
    randomly within given interval
    :param G: matrix that represents graph - its a neighbour matrix
    :param min: lower boundary for generated weights
    :param max: upper boundary for generated weights
    :return: two matrixes thet represents the digraph - first one is neighbour matrix,
    second one is a matrix with the digraph's edges weights
    """
    neigh_matrix = from_list_to_neighbour_matrix(G)
    weight_matrix = from_list_to_neighbour_matrix(G)
    size = len(neigh_matrix)
    for i in range(size):
        for j in range(size):
            if neigh_matrix[i][j] == 1:
                tmp = random.randint(min, max)
                weight_matrix[i][j] = tmp
            else:
                weight_matrix[i][j] = None
    return neigh_matrix, weight_matrix


def bellman_ford_algorithm(G, src):
    """
    Function that finds shortest paths from given vertex of the digraph
    (using bellman-ford algorithm)
    Function also checks if digraph has a negative cycle
    :param G: digraph, represented by matrix containing weight of its every edge or
    None if there is no connection between particular two vertexes
    :param src: the vertex from which we will start every path
    :return: an array representing distances between given vertex (src) and every vertex of the digraph
    or a boolenan False if digraph has a negative cycle
    """
    connections = []
    for u in range(len(G)):
        for v in range(len(G[0])):
            if G[u][v] != None:
                connections.append([u, v, G[u][v]])

    vertices = len(G)
    edges = len(connections)

    #initialize distance array with max possible distances and 0 for given vertex - src
    distance = [float("Inf")] * vertices
    distance[src] = 0

    #do relax for every edge done n-1 times (n-number of vertexes)
    #if there is no negative cycle, it should result with an array of shortest possible paths
    for i in range(vertices - 1):
        for j in range(edges):
            x = connections[j][0]
            y = connections[j][1]
            weight = connections[j][2]
            if distance[x] + weight < distance[y]:
                distance[y] = distance[x] + weight

    #check if has negative cycle, if so - communicate that and return
    for i in range(edges):
        x = connections[i][0]
        y = connections[i][1]
        weight = connections[i][2]
        if distance[x] != float("Inf") and distance[x] + weight < distance[y]:
            #if we managed to find shorter path than before, that means there is a nagative cycle
            print("Graf zawiera ujemny cykl!")
            return False

    #if there is no negative cycle, return array of distances
    return distance


def solve_bellman_ford(digraph):
    """
    Function to calculate shortest paths in given digraph using bellman-ford algorithm.
    :param digraph: digraph, represented by matrix containing weight of its every edge and
    None if there is no connection between particular two vertexes
    :return: matrix containing distances between vertexes in digraph - value on position in
    row w and col k is the shortest possible path from vertex w to k
    """
    bell_digraph = []
    for i in range(len(digraph)):
        check = bellman_ford_algorithm(digraph, i)
        if check:
            bell_digraph.append(check)
        else:
            return False
    # matrix of shortest possible paths, value in row w and column k is the shortest path from vertex w to k
    return bell_digraph


def add_s(G):
    """
    Helper function for johnson algorithm - it adds an extra vertex to given digraph,
    and the additional vertex gets a path (with weight = 0) to every other vertes in the digraph
    :param G: digraph, represented by matrix containing weight of its every edge and
    None if there is no connection between particular two vertexes
    :return: copied G digraph but extended with one extra vertex, containing weights of edges or
    None if there is no connection
    """
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


def dijkstra_algorithm(G, s):
    """
    Helper function for johnson's algorithm, for digraphs with no negative weights.
    It calculates, for the given digraph, shortes distances from vertex s to every
    vertex in the digraph.
    :param G: digraph, represented by matrix containing weight of its every edge and
    None if there is no connection between particular two vertexes
    :param s: index of vertex to start every path from
    :return: an array of shortest possible distances between s and every vertex in G
    """
    distances = [float('inf')] * len(G)
    distances[s] = 0
    waiting = []
    for i in range(len(G)):
        waiting.append(i)

    for _ in range(len(G)):
        current = waiting[0]
        for j in waiting:
            if distances[j] < distances[current]:
                current = j
        waiting.remove(current)

        for vertice in waiting:
            if G[current][vertice] != None:
                if distances[vertice] > distances[current] + G[current][vertice] :
                    distances[vertice] = distances[current] + G[current][vertice]

    return distances


def johnson_algorithm(G):
    """
    Function which calculates shortest paths between every pair of vertexes in digraph.
    :param G: matrix representing digraph - contains weights for every existing edge or
    None f there is no edge between vertexes.
    :return: matrix containing distances between vertexes in digraph G - value on position in
    row w and col k is the shortest possible path from vertex w to k
    or, if there is negative cycle in G digraph, then the function just shows a message and returns
    """
    Gs = add_s(G)
    #first add extra vertex with edges leading to every other vertex with weights 0
    h = bellman_ford_algorithm(Gs, len(Gs)-1)
    if not h:
        #check if there is negative cycle, if so - return
        print("It's not possible to use johnson's algorithm for this digraph, becouse it has a negative cycle!")
        return
    else:
        #first scale weights to make them positive ( negative weights make it impossible to use dijkstra later)
        new_weights = []
        for i in range(len(Gs)):
            new_weights.append([])
            for j in range(len(Gs)):
                if Gs[i][j] != None:
                    new_weights[i].append(Gs[i][j] + h[i] - h[j])
                else:
                    new_weights[i].append(None)

        #we get rid of the extra vertex we added before - we don't need it anymore
        #also, we create an array of distances to use later
        reduced_weights = []
        D =[]
        for i in range(len(G)):
            D.append([])
            reduced_weights.append([])
            for j in range(len(G)):
                D[i].append(0)
                reduced_weights[i].append(new_weights[i][j])

        for i in range(len(G)):
            #there are no negative weights so we can use dijkstra
            #we run dijkstra multiply times for every vertex
            distances = dijkstra_algorithm(reduced_weights, i)
            for j in range(len(G)):
                #we calculate final distances by scaling dijkstra desults again
                D[i][j] = distances[j] - h[i] + h[j]
        # matrix of shortest possible paths, value in row w and column k is the shortest path from vertex w to k
        return D


if __name__ == "__main__":
    #ex3
    print('EX 3')
    bf_solved = False
    number_of_tries = 0
    while not bf_solved:
        number_of_tries += 1
        test_digraph = generate_random_strongly_coherent_digraph(5, 0.5)
        neigh_matrix, weight_matrix = add_randomized_weights_to_digraph(test_digraph, -5, 10)
        bf_solved = solve_bellman_ford(weight_matrix)
        if bf_solved:
            # print("Managed to generate randomized stongly coherent digraph with random weights with no negative cycle in ", number_of_tries, "tries")
            print_neigh_matrix_in_decent_way(weight_matrix)
            print_neigh_matrix_in_decent_way(bf_solved)
            j_solved = johnson_algorithm(weight_matrix)
            print_neigh_matrix_in_decent_way(j_solved)


    #ex4
    digraph1 = [
        [None, -1, -4],
        [4, None, None],
        [None, 2, None]
    ]

    digraph2 = [
        [None, 6, 3, None, -1, None, None],
        [10, None, -5, -4, 4, None, 4],
        [None, None, None, None, None, 2, None],
        [None, 5, None, None, None, None, 9],
        [None, None, None, None, None, None, -4],
        [None, 9, None, None, None, None, None],
        [None, None, None, None, None, 4, None]
    ]

    print('EX 4')
    johnsolved = johnson_algorithm(digraph1)
    print_neigh_matrix_in_decent_way(johnsolved)

    johnsolved = johnson_algorithm(digraph2)
    print_neigh_matrix_in_decent_way(johnsolved)




