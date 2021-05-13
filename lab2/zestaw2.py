import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import collections
import random
import time

def calculate_nodes_position(n_of_nodes):
    """
    Function calculates position of the nodes.
    :param n_of_nodes: an integer which represents number of nodes
    :return nodes: a dictionary which contains a number of node as a key a tuple with coordinates as a value.
    """
    
    nodes = {}
    for n in range(0, n_of_nodes):
        x = math.cos(2 * math.pi / n_of_nodes * n)
        y = math.sin(2 * math.pi / n_of_nodes * n)
        nodes.update({n: (x, y)})
    return nodes
	
def create_graph_visualization(matrix):
    """
    Function visualizes the matrix of neighbourhood of graph
    :param matrix: it's a numpy matrix, so using our functions from previous module
                    it is needed to be converted by numpy.matrix
    :return: None
    """
    sizes = matrix.shape
    if len(sizes) != 2 or sizes[0] != sizes[1]:
        print("Incorrect matrix!")
        return
    if len(matrix) > 0:
        nodes = calculate_nodes_position(len(matrix))
        plt.figure(figsize=(5, 5))
        graph_visualization = nx.from_numpy_matrix(matrix)
        nx.draw_networkx(graph_visualization, nodes, node_color="#FFE55E", font_size=15)
        plt.show()
    else:
        print("Empty matrix!")
		
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
    return matrix
	
def bubble_sort(arr):
    """
        Function uses bubble sort algorithm to sort a list.
        :param arr: it's a not empty list 
        :return arr: sorted list.
    """
    
    temp = 0
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
	
def calculate_odd_elements(arr):
    """
        Function calcuates the number of odd element in a list.
        :param arr: it's a not empty list 
        :return isDegreeSeq: boolean value - False when there is odd number of odd elements, True when there is even number of odd elements.
    """
    
    counter = 0;
    isDegreeSeq = True;
    for i in range(0, len(arr)):
        if arr[i] % 2 == 1:
            counter = counter + 1
    if counter % 2 == 1:
        isDegreeSeq = False
    return isDegreeSeq
	
def degree_seq(arr):
    """
        Function check if the list represents a degree sequence or not.
        :param arr: it's a non empty list 
        :return boolean: boolean value - True if the list represents a degree sequence, otherwise False.
    """
    
    if calculate_odd_elements(arr):
        arr = bubble_sort(arr)
        while True:
            allZeros = all(elem == 0 for elem in arr)
            if allZeros == True:
                return allZeros
            isNegative = False
            for i in range(1, len(arr)):
                if arr[i] < 0:
                    isNegative = True
            if arr[0] < 0 or arr[0] >= len(arr) or isNegative:
                return False
            for i in range(1, arr[0]+1):
                arr[i] = arr[i] - 1
            arr[0] = 0
            arr = bubble_sort(arr)
    else:
        return False
		
def sum(arr):
    
    """
        Function calculates a sum of the list elements.
        :param arr: it's not empty list
        :return sum: integer which represents a sum of list elements.
    """
    
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    return sum
	
def check_matrix_correctness(matrix, degrees):
    
    """
        Function check if the number of edges from each vertex is equal to a number represents degree of each vertex.
        :param matrix: not empty array of arrays which represents graph
        :param degrees: not empty array which represents vertices degrees of the graph
        :return errorsArr: an array which contains an indexes of incorrect vertices.
    """
    
    errorsArr = []
    tmp = 0
    for i in range(len(matrix)):
        tmp = sum(matrix[i])
        if tmp != degrees[i]:
            errorsArr.append(i)
    return errorsArr
	
def sort_in_reverse_order(list):
    
    """
        Function sorts an array of arrays in reverse order.
        :param list: an unsorted array of arrays
        :return : None. 
    """
    
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i][1] < list[j][1]:
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp
				
def create_graph_from_seq(arr):
    
    """
        Function creates a graph based on the degree sequence represented by an array arr.
        :param arr: an array which represents a degree sequence
        :param matrix or []: an array of arrays which represents a graph.
    """
    
    arr = bubble_sort(arr)
    matrix = [[0 for i in range(len(arr))] for j in range(len(arr))]
    listOfIndexesAndDegrees = []
    for i in range(len(arr)):
        listOfIndexesAndDegrees.append([i, arr[i]])
           
    if degree_seq(arr):
        while True:
            allZeros = True
            for i in range(len(arr)):
                if listOfIndexesAndDegrees[i][1] != 0:
                    allZeros = False
            if allZeros and check_matrix_correctness(matrix, arr):
                return matrix
            isNegative = False
            for i in range(1, len(arr)):
                if listOfIndexesAndDegrees[i][1] < 0:
                    isNegative = True
            if listOfIndexesAndDegrees[0][1] < 0 or listOfIndexesAndDegrees[0][1] >= len(arr) or isNegative:
                return []
            for i in range(1, listOfIndexesAndDegrees[0][1] + 1):
                matrix[listOfIndexesAndDegrees[0][0]][listOfIndexesAndDegrees[i][0]] = 1
                matrix[listOfIndexesAndDegrees[i][0]][listOfIndexesAndDegrees[0][0]] = 1
                listOfIndexesAndDegrees[i][1] = listOfIndexesAndDegrees[i][1] - 1
            listOfIndexesAndDegrees[0][1] = 0
            sort_in_reverse_order(listOfIndexesAndDegrees)
    else:
        return []
		
def generate_k_regular_graph(k, numOfVertices):
    
    """
        Function creates a k regular graph.
        :param k: an integer which is a degree of each vertex
        :param numOfVertices: an integer which describes a number of vertices
        :return matrix: an array of arrays which represents a graph
    """
    
    arr = []
    for i in range(numOfVertices):
        arr.append(k)
    return create_graph_from_seq(arr)
	
def randomize(graph, number):
    
    """
        Function randomize a graph by changing a vertices ab and cd to ad and bc.
        :param graph: an array of arrays which represents the graph
        :param number: an integer which represents a number of randomizations
        :return : None
    """
    
    if len(graph) > 0:
        for rands in range(number):
            i = 0
            size = len(graph)-1
            firstIdx = random.randint(0, size)
            secondIdx = random.randint(0, size)
            while graph[firstIdx][secondIdx] != 1:
                firstIdx = random.randint(0, size)
                i = 0
                while firstIdx == secondIdx:
                    secondIdx = random.randint(0, size)
                    i = i + 1
                    if i == 100:
                        break
                if i == 100:
                    break
            if i == 100:
                print("Couldn't randomize graph!")
                return
            i = 0
            thirdIdx = random.randint(0, size)
            fourthIdx = random.randint(0, size)
            while thirdIdx == firstIdx or thirdIdx == secondIdx or graph[thirdIdx][fourthIdx] != 1:
                thirdIdx = random.randint(0, size)
                while thirdIdx == fourthIdx or fourthIdx == firstIdx:
                    fourthIdx = random.randint(0, size)
                    i = i + 1
                    if i == 100:
                        break
                if i == 100:
                    break
            if i == 100:
                print("Couldn't randomize graph!")
                return
            #print("firstIdx = " + str(firstIdx) + " secondIdx = " + str(secondIdx) + " thirdIdx = " + str(thirdIdx) + " fourthIdx = " + str(fourthIdx))
            if firstIdx != fourthIdx and firstIdx != secondIdx and thirdIdx != fourthIdx and secondIdx != thirdIdx and graph[firstIdx][fourthIdx] == 0 and graph[secondIdx][thirdIdx] == 0:
                graph[firstIdx][secondIdx] = 0
                graph[secondIdx][firstIdx] = 0
                graph[firstIdx][fourthIdx] = 1
                graph[fourthIdx][firstIdx] = 1
                graph[thirdIdx][fourthIdx] = 0
                graph[fourthIdx][thirdIdx] = 0
                graph[secondIdx][thirdIdx] = 1
                graph[thirdIdx][secondIdx] = 1
				
def components_r(nr, v, graph, comp):
    
    """
        Function represents implementation of DFS algorithm.
        :param nr: an integer which represents a number of component
        :param v: an integer which represents a number of the vertex
        :param graph: a dictionary in which keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge 
        :param comp: an array which stores numbers, that numbers represents an index of each component
        :return : None.
    """
    
    for j in range(len(graph.get(v))):
        if comp[graph.get(v)[j]-1] == -1:
            comp[graph.get(v)[j]-1] = nr
            components_r(nr, graph.get(v)[j], graph, comp)
			
def components(graph):
    
    """
        Function creates and prints a list of graph components.
        :param graph: a dictionary in which keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
        :return : None.
    """
    
    nr = 0
    comp = [-1 for i in range(len(graph))]
    for i in range(len(graph)):
        if comp[i] == -1:
            nr = nr + 1
            comp[i] = nr
            components_r(nr, i+1, graph, comp)
    counter = 0
    dicto = {}
    for i in range(len(comp)):
        if comp[i] != counter:
            counter = comp[i]
            dicto[counter] = []
    for i in range(len(comp)):
        dicto[comp[i]].append(i+1)
    sorted_dict = collections.OrderedDict(sorted(dicto.items()))
    temp = ""
    for i in range(1, len(sorted_dict)+1):
        temp = temp + str(i) + ") "
        for elem in sorted_dict[i]:
            temp = temp + str(elem) + " "
        print(temp)
        temp = ""
    longest = -1
    longest_dict_idx = 0
    for i in range(1, len(sorted_dict)+1):
        if len(sorted_dict[i]) > longest:
            longest = len(sorted_dict[i])
            longest_dict_idx = i
    print("Najwieksza skladowa ma numer " + str(longest_dict_idx) + ".")
	
def getNumberOfComponents(graph):
    
    """
        Function creates a dictionary of graph components. It returns a length of the dictionary 
        which represents the number of components.
        :param graph: a dictionary in which keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
        :return len(sorted_dict): an integer which represents a numbre of components.
    """
    
    nr = 0
    comp = [-1 for i in range(len(graph))]
    for i in range(len(graph)):
        if comp[i] == -1:
            nr = nr + 1
            comp[i] = nr
            components_r(nr, i+1, graph, comp)
    counter = 0
    dicto = {}
    for i in range(len(comp)):
        if comp[i] != counter:
            counter = comp[i]
            dicto[counter] = []
    for i in range(len(comp)):
        dicto[comp[i]].append(i+1)
    sorted_dict = collections.OrderedDict(sorted(dicto.items()))
    return len(sorted_dict)
	
def find_euler_cycle(cycle, idx, graph, isolatedVertices):
    
    """
        Function returns an array which represents Euler cycle.
        :param cycle: an array which stores an indexes of vertices
        :param idx: an integer which represents an index of vertex
        :param graph: an array of arrays which represents a graph
        :param isolatedVertices: an integer which represents a number of isolated components
        :return : None.
    """
    
    for j in range(len(graph[idx])):
        if graph[idx][j] != 0:
            graph[idx][j] = 0
            graph[j][idx] = 0
            if getNumberOfComponents(from_matrix_neighbour_to_list(graph)) - isolatedVertices > 1:
                if not 1 in graph[j] and not 1 in graph[idx]:
                    isolatedVertices = isolatedVertices + 1
                    cycle.append(j+1)
                    cycle.append(idx+1)
                    return
                elif not 1 in graph[j] and 1 in graph[idx]:
                    graph[idx][j] = 1
                    graph[j][idx] = 1
                else:
                    isolatedVertices = isolatedVertices + 1
                    find_euler_cycle(cycle, j, graph, isolatedVertices)
            else:
                find_euler_cycle(cycle, j, graph, isolatedVertices)
    cycle.append(idx+1)
	
def prepare_random_vertices(numberOfVertices):
    
    """
         Function creates a degree sequence which contains Euler cycle.
         :param numberOfVertices: an integer which represents a length of generated array
         :return vertices: an array which represents a degree sequence.
    """
    
    vertices = [-1 for i in range(numberOfVertices)]
    for i in range(numberOfVertices):
        randNum = random.randint(1, numberOfVertices)
        while (randNum % 2 != 0 or randNum == numberOfVertices):
            randNum = random.randint(1, numberOfVertices)
        vertices[i] = randNum
        if i == numberOfVertices - 1:
            copy = vertices.copy()
            if degree_seq(copy) == False:
                vertices = prepare_random_vertices(numberOfVertices)
    return vertices
	
def generate_euler_graph(numberOfVertices):
    
    """
        Function generates random Euler graph with given number of vertices.
        :param numberOfVertices: an integer which specify a length of an array
        :return : None.
    """
    
    if numberOfVertices < 3:
        print(" ")
        return
    vertices = prepare_random_vertices(numberOfVertices)
    #graph = from_list_to_matrix_neighbour({1: [2,6], 2: [1,3,5,6], 3: [2,4,5,6], 4: [3,5], 5: [2,3,4,6], 6: [1,2,3,5]})
    #graph = from_list_to_matrix_neighbour({1: [2,3,9,10], 2: [1,3,9,10], 3: [1,2,4,8,9,10], 4: [3,5,6,7,8,9], 5: [4,6,7,8], 6: [4,5,7,8], 7: [4,5,6,8], 8: [3,4,5,6,7,9], 9: [1,2,3,4,8,10], 10: [1,2,3,9]})
    #graph = from_list_to_matrix_neighbour({1: [2,3,4,5], 2: [1,5,6,7], 3: [1,4], 4: [1,3], 5: [1,2], 6: [2,7], 7: [2,6]})
    graph = create_graph_from_seq(vertices)
    while getNumberOfComponents(from_matrix_neighbour_to_list(graph)) != 1:
        vertices = prepare_random_vertices(numberOfVertices)
        graph = create_graph_from_seq(vertices)
    create_graph_visualization(np.matrix(graph))
    #print(from_matrix_neighbour_to_list(graph))
    cycle = []
    find_euler_cycle(cycle, 0, graph, 0)
    path = ""
    for i in range(len(cycle)):
        if i == 0:
            path = path + str(cycle[len(cycle)-1])
        else:
            path = path + " - " + str(cycle[len(cycle)-1-i])
    print(path)
	
def modified_components_r(v, graph, comp, stack):
    
    """
        Function checks if there is a Hamilton cycle in the graph or not.
        :param v: number of vertex
        :param graph: a dictionary in which keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
        :param comp: an array which contains an information about visited vertices
        :param stack: an array which contains an indexes of visited vertices
        :return : None.
    """
    
    for i in graph.get(v):
        if comp[i-1] == -1:
            comp[i-1] = 1
            stack.append(i)
            if len(stack) == len(graph):
                if not stack[0] in graph.get(i):
                    tmp = stack.pop()
                    comp[tmp-1] = -1
                else:
                    stack.append(stack[0])
            else:
                modified_components_r(i, graph, comp, stack)
                if len(stack) <= len(graph): # Ścieżka hamiltona w grafie ma o 1 wierzchołek więcej od wierzchołków grafu
                    tmp = stack.pop()
                    comp[tmp-1] = -1
					
def find_hamilton_cycle(graph):
    
    """
        Function looks for a Hamilton cycle in the given graph. It prints out the Hamilton cycle based on the vertices from 
        the stack or prints the information that there is no Hamilton cycle in the graph.
        :param graph: a dictionary in which keys are numbers of graph vertex and values
                    are lists of other vertexes connected with them by edge
        :return : None.
    """
    if len(graph) < 20 and getNumberOfComponents(graph) == 1:
        comp = [-1 for i in range(len(graph))]
        stack = []
        for i in range(len(graph)):
            if comp[i] == -1:
                comp[i] = 1
                stack.append(i+1)
                modified_components_r(1, graph, comp, stack)
        if len(stack) == len(graph)+1:
            tmpStr = "["
            for i in range(len(stack)):
                if i < len(stack)-1:
                    tmpStr = tmpStr + str(stack[i]) + " - "
                else:
                    tmpStr = tmpStr + str(stack[i]) + "]"
            print(tmpStr)
        else:
            print("No hamilton cycle in this graph!")