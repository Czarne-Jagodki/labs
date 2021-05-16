import ex1
import numpy as np
import random

"""
Nie dziala dla pustych list sasiedztwa
"""
def DFS_Visit(v, G, d, f, t):
    t = t + 1
    d[v] = t
    #print("BERORE" + str(t))

    for neighbour_v in G[v]:
        if d[neighbour_v] == -1:
            t = DFS_Visit(neighbour_v, G, d, f, t)
    t = t + 1
    f[v] = t
    #print("AFTER"+ str(t))
    return t


def components_R(nr, v, G_Trans, comp):
    try:
        if G_Trans[v] == []:
            print("KURwa")
        for neighbour_v in G_Trans[v]:
            if comp[neighbour_v] == -1:
                comp[neighbour_v] = nr
                components_R(nr,neighbour_v, G_Trans, comp)
    except:
        print("COMPONENT ERROR")


def revert_matrix_values(list_neighbours):
    #print(matrix)
    #list_from_matrix = ex1.from_matrix_neighbour_to_list(matrix)
    incidence_matrix = ex1.from_list_to_incidence_matrix(list_neighbours)
    shape = np.shape(incidence_matrix)
    rows = 0
    columns = 1
    #print(incidence_matrix)
    for row in range(shape[rows]):
        for column in range(shape[columns]):
            if incidence_matrix[row,column] == 1:
                incidence_matrix[row,column] = -1
            elif incidence_matrix[row,column] == -1:
                incidence_matrix[row,column] = 1
    return ex1.from_incidence_matrix_to_list(incidence_matrix)
    # for row in incidence_matrix:
    #     print(len(row[0]))

    #print(incidence_matrix)


def kosaraju(G):
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
    #print(len(G))
    for v in G_trans.keys():
        comp[v] = -1
    #print(comp)
    #print(G)
    #print(G_trans)
    #print(f)
    # print(dict( sorted(f.items(),key=lambda item: item[1],reverse=True)))
    # print(comp)
    edges = G_trans
    # print(edges)
    for v in dict( sorted(f.items(),key=lambda item: item[1],reverse=True)).keys():
        # print(v)
        #print(comp[v])
        try:
            if comp[v] == -1:
                nr = nr + 1
                comp[v] = nr
                components_R(nr,v, G_trans, comp)
        except:
            print("KOsaraju error")
    #print(f)
    #print(comp)
    return comp


# n = 10
# p = 0.5
# matrix = ex1.rand_digraph_with_probability(n,p)
# list_matrix = ex1.from_matrix_neighbour_to_list(matrix)
#
# revert_matrix_values(list_matrix)
#
# result = kosaraju(list_matrix)
# print(list_matrix)
# print(result)




