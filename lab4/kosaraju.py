import ex1
import numpy as np

def DFS_Visit(v, G, d, f, t):
    """
    DFS algorithm
    :param v: vertex of graph
    :param G: graph in list of neighbours
    :param d: list of visiting times
    :param f: list of going through vertex
    :param t: time
    :return: t
    """
    t = t + 1
    d[v] = t

    for neighbour_v in G[v]:
        if d[neighbour_v] == -1:
            t = DFS_Visit(neighbour_v, G, d, f, t)
    t = t + 1
    f[v] = t

    return t


def components_R(nr, v, G_Trans, comp):
    """

    :param nr: number of cluster
    :param v: vertex
    :param G_Trans: reverse matrix to entry matrix
    :param comp: array of clusters
    :return:
    """
    if v not in G_Trans:
        nr = nr + 1
        comp[v] = nr
        return
    for neighbour_v in G_Trans[v]:
        if neighbour_v not in comp:
            # nr = nr + 1
            # print(neighbour_v)
            # comp[neighbour_v] = nr
            # print(comp)
            # components_R(nr, neighbour_v, G_Trans, comp)
            print()
        elif comp[neighbour_v] == -1:
            # nr = nr + 1
            comp[neighbour_v] = nr
            components_R(nr,neighbour_v, G_Trans, comp)


def revert_matrix_values(list_neighbours):
    """
    Function returns reversed graph
    :param list_neighbours: graph in list of neighbours
    :return: list of neighbours but reversed to the entry list
    """
    incidence_matrix = ex1.from_list_to_incidence_matrix(list_neighbours)
    shape = np.shape(incidence_matrix)
    rows = 0
    columns = 1

    for row in range(shape[rows]):
        for column in range(shape[columns]):
            if incidence_matrix[row,column] == 1:
                incidence_matrix[row,column] = -1
            elif incidence_matrix[row,column] == -1:
                incidence_matrix[row,column] = 1
    return ex1.from_incidence_matrix_to_list(incidence_matrix)

def sort_f(f):
    """
    Funcion helps to sort times
    :param f:
    :return:
    """
    return dict(sorted(f.items(), key=lambda item: item[1], reverse=True)).keys()

def sort_G_by_f(G, f):
    """
    Function sorts Graph using times
    :param G:
    :param f:
    :return:
    """
    new_G = {}
    for element in f:
        try:
            new_G[element] = G[element]
        except:
            new_G[element] = []
    return new_G

def kosaraju(G):
    """
    Kosaraju algorithm
    :param G: grapgh represented as list of neighbours
    :return: dictionary - vertex and cluster where vertex fits
    """
    d = {}
    f = {}
    for v in G.keys():
        d[v] = -1
        f[v] = -1
    t = 0
    for v in G.keys():
        if d[v] == -1:
            DFS_Visit(v, G, d, f, t)
    G_trans = revert_matrix_values(G)
    nr = 0

    comp = {}

    for v in G_trans.keys():
        comp[v] = -1

    for v in sort_G_by_f(G_trans, sort_f(f)).keys():

        if v not in comp:
            nr = nr + 1
            comp[v] = nr

        elif comp[v] == -1:
            nr = nr + 1
            comp[v] = nr
            components_R(nr, v, G_trans, comp)

    return comp

def group_result(input):
   """
   Functions groups the results of kosaraju function to clusters which are represented by dictonary and list
   :param input:  result from kosaraju function
   :return: dictionaty with key - number of cluster , value - array of vertexes which fit to cluster
   """
   results = dict(sorted(input.items(), key=lambda item: item[1]))
   list_of_results = {}

   for key, value  in results.items():
       if value not in list_of_results:
          temp = []
          temp.append(key)
          list_of_results[value] = temp
       else:
           list_of_results[value].append(key)

   return list_of_results

n = 15
p = 0.1
matrix = ex1.rand_digraph_with_probability(n,p)
list_matrix = ex1.from_matrix_neighbour_to_list(matrix)
#
# revert_matrix_values(list_matrix)
#
result = kosaraju(list_matrix)
print(list_matrix)
print(result)
print(group_result(result))

# list_my = {
#           1 : [2],
#           2 : [1],
#           3 : [5],
#           4 : [5],
#             5: [3],
# }
# res= kosaraju(list_my)
# print()
# print(list_my)
# print(res)
# print(group_result(res))



