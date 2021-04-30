from random import randrange
from random import random

def rand_graph_A(n,l):
    """
    Functions draw the graph. It draws l edges between vertexes.
    Function chooses random vertexes and if they're not connected it links them.
    :param n: number of vertexes
    :param l: number of edges
    :return: array of arrays represents matrix of neighbourhood of graph
    """
    if l > (n * (n - 1)/2):
        print("Cannot draw this graph, too many edges")
        return None
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
    """
    Functions draw the graph using probability that between two vertexes exists edge
    :param n: number of vertexes
    :param p: probability -> it is between [0,1]
    :return: array of arrays represents matrix of neighbourhood of graph
    """
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if(p > random()):
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix
#ex1.print_matrix(rand_graph_B(5,0.5))