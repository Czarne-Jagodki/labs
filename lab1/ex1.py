def print_matrix(matrix):
    i = 0
    for row in matrix:
        i = i + 1
        print(i, end='. ')
        print(row)

def print_list(list):
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

from_list_to_matrix_neighbour(neighbour_list)

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

#from_matrix_neighbour_to_list(from_list_to_matrix_neighbour(neighbour_list))

def from_list_to_incidence_matrix(list):
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

    print_matrix(matrix)
    return matrix

#from_list_to_incidence_matrix(neighbour_list)

def from_incidence_matrix_to_list(matrix):
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
    #print_list(list)
    return list

#from_incidence_matrix_to_list(from_list_to_incidence_matrix(neighbour_list))