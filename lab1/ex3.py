from random import randrange
from random import random
import ex1

#function chooses random vertexes and if they're not connected it links them
#while l is bigger than 0
def rand_graph_A(n,l):
    matrix = [[0 for i in range(n)] for j in range(n)]
    while(l > 0):
        i = randrange(0, n)
        j = randrange(0, n)
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            matrix[j][i] = 1
            l = l - 1

    return matrix

#ex1.print_matrix(rand_graph_A(5,7))

#probability is between 0 and 1
#function goes through half of matrix and decide if between two vertex is edge or not
def rand_graph_B(n,p):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if(p > random()):
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix
#ex1.print_matrix(rand_graph_B(5,0.5))