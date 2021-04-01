from random import randrange
import ex1

#seed(1)
def rand_graph_A(n,l):
    matrix = [[0 for i in range(n)] for j in range(n)]
    while(l > 0):
        i = randrange(0, n)
        j = randrange(0, n)
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            matrix[j][i] = 1
            l = l - 1

    #print_matrix(matrix)
    return matrix

rand_graph_A(5,5)
