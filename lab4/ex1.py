'''
EVery input with matrix is np.matrix bro
'''
def print_list(list):
    """
    Function shows a list of neighbourhood of graph.
    It show appropriate vertex and other vertexes connected with it
    :param list: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    :return: None
    """
    for key, value in list.items():
        print(key, end=' -> ')
        print(value)

neighbour_list = {
          1 : [2, 5],
          2 : [1, 3, 5],
          3 : [2, 4, 5],
          4 : [3],
          5 : [1, 2]
}
def print_matrix(matrix):
    """
        Function shows a matrix of neighbourhood of graph.
        :param list: it's a not empty array of arrays
        :return: None
        """
    i = 0
    for row in matrix:
        i = i + 1
        print(i, end='. ')
        print(row)

import ex2
import numpy as np
def from_list_to_matrix_neighbour(list):
    """
    Function converts neighbourhood list to neighbourhood matrix of digraph
    :param list: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    :return: np.matrix which represents neighbourhood matrix of digraph
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
    return np.matrix(matrix)

m = from_list_to_matrix_neighbour(neighbour_list)
#ex2.create_graph_visualization(m)

def from_matrix_neighbour_to_list(matrix):
    """
        Function converts neighbourhood matrix to neighbourhood list
        :param matrix: not empty np.matrix which represents graph
        :return: it's a dictionary: keys are numbers of graph vertex and values
                        are lists of other vertexes connected with them by edge
    """

    list = {}
    vertex_number = 0
    for row in matrix:
        vertex_number += 1
        row_list = []
        destination_number = 0
        for element_in_row in np.nditer(row):
            if element_in_row == 1:
                row_list.append(destination_number  + 1)
            destination_number  += 1
        list[vertex_number] = row_list
    return list

l = from_matrix_neighbour_to_list(m)
#print_list(l)

def transpone_matrix(matrix):
    """
    Function to transpone matrix
    It's needed, beceuse inside incidence functions we work on array of arrays
    :param matrix: not empty array of arrays
    :return:  array of arrays but transponed
    """
    import numpy as np
    n = np.matrix(matrix)
    n = n.transpose()
    new_matrix = []
    n = np.array(n)
    for row in n:
        new_matrix.append(row)
    return new_matrix

def from_list_to_incidence_matrix(list):
    """
    Function converts list of neighbourhood to incidence matrix
    :param list: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    :return: it's a array of arrays which represents incidence matrix of graph
    """
    matrix = []

    for key, value in list.items():
        for elem in value:
            row = [0] * len(list)
            row[key - 1] = -1
            row[elem - 1] = 1
            matrix.append(row)
    matrix = transpone_matrix(matrix)
    return np.matrix(matrix)

m = from_list_to_incidence_matrix(l)
#print_matrix(m)

def from_incidence_matrix_to_list(matrix):
    """
    Function converts incidence matrix to list of neighbourhood
    :param matrix: it's a not empty np.matrix represents incidence matrix of digraph,
    :return: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    """
    matrix = transpone_matrix(matrix)
    list = {}
    for row in matrix:
        source = -1
        destination = -1
        for elem_in_row in range(len(row)):
            if row[elem_in_row] == 1:
                destination = elem_in_row
            if row[elem_in_row] == -1:
                source = elem_in_row
        if source+1 in list:
            list[source+1].append(destination+1)
        else:
            list[source+1] = [destination+1]
    #print_list(list)
    l = {}
    for key in sorted(list):
        l[key] = list[key]
    list = l
    return list

l = from_incidence_matrix_to_list(m)
#print_list(l)

from random import random
def rand_digraph_with_probability(n,p):
    """
    Functions draw the graph using probability that between two vertexes exists edge
    :param n: number of vertexes
    :param p: probability -> it is between [0,1]
    :return: np.matrix represents matrix of neighbourhood of graph
    """
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(i == j):
                continue
            if(p > random()):
                matrix[i][j] = 1
    return np.matrix(matrix)

#print_list(from_matrix_neighbour_to_list(rand_digraph_with_probability(10,1)))
#ex2.create_graph_visualization(rand_digraph_with_probability(100,0.01))