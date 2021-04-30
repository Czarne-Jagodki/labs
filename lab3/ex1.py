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
          3 : [2, 4],
          4 : [3, 5],
          5 : [1, 2, 4]
}

def from_list_to_matrix_neighbour(list):
    """
    Function converts neighbourhood list to neighbourhood matrix
    :param list: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    :return:  array of arrays which represents graph
    """
    matrix = []
    length = len(list)
    for elements in list.values():
        row = []
        for i in range(1, length + 1):
            if i in elements:
                row.append(1)
            else :
                row.append(0)
        matrix.append(row)
    print_matrix(matrix)
    return matrix

#from_list_to_matrix_neighbour(neighbour_list)

def from_matrix_neighbour_to_list(matrix):
    """
    Function converts neighbourhood matrix to neighbourhood list
    :param matrix: not empty array of arrays which represents graph
    :return: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    """
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

#from_matrix_neighbour_to_list(from_list_to_matrix_neighbour(neighbour_list))

def transpone_matrix(matrix):
    """
    Function to transpone matrix
    It's needed, beceuse functions associated with incidence returned not appropriate results
    :param matrix: not empty array of arrays
    :return:  array of arrays but transponed
    """

    import numpy as np
    n = np.matrix(matrix)
    n = n.transpose()
    length = len(n)
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
        ranger = key        #ranger check if we do not use element used
                            # in previous iterations to prevent from doubling same row
        for elem in value:
            if ranger < elem:
                row = [0] * len(list)
                row[key - 1] = 1
                row[elem - 1] = 1
                matrix.append(row)

    #print_matrix(matrix)
    matrix = transpone_matrix(matrix)
    return matrix

# print_matrix(from_list_to_incidence_matrix(neighbour_list))

def from_incidence_matrix_to_list(matrix):
    """
    Function converts incidence matrix to list of neighbourhood
    :param matrix: it's a not empty array of arrays represents incidence matrix of graph,
                    the matrix must be transponed on the input
                    if it does not become from functions from this module
                    The best way to do it is by our previous function
    :return: it's a dictionary: keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
    """
    matrix = transpone_matrix(matrix)
    list = {}
    for row in matrix:
        i = -1
        j = -1
        for k in range(len(row)):
            if row[k] == 1:
                if i != -1:
                  j = k + 1
                else:
                    i = k + 1
        if i in list:
            list[i].append(j)
        else:
            list[i] = [j]

        if j in list:
            list[j].append(i)
        else:
            list[j] = [i]

    l = {}
    for key in sorted(list):
        l[key] = list[key]
    list = l
    return list

if __name__ == '__MAIN__':
    print_list(from_incidence_matrix_to_list(from_list_to_incidence_matrix(neighbour_list)))

