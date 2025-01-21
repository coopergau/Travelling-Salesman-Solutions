from collections import namedtuple
import random
import numpy as np

def generate_nodes(amount, map_length):
    ''' Generates unique randomly positioned nodes. '''
    Node = namedtuple('Node', ['x', 'y'])
    nodes = []
    while len(nodes) < amount:
        new_node = Node(random.uniform(0, map_length), random.uniform(0, map_length))
        if new_node not in nodes:
            nodes.append(new_node)
    return nodes

def create_distance_matrix(nodes):
    '''
    Create the distance matrix D to represent the distances between all nodes. D has dimensions n x n, where n is the amount of nodes 
    on the map. The entry at position (i,j) in the matrix represents the distance between node i and node j. The nodes are numbered 
    according to their order of creation. If i=j, the distance will be set infinty so it is never selected as an option.
    '''
    num_of_nodes = len(nodes)
    d_matrix = np.empty((num_of_nodes, num_of_nodes))
    for row in range(num_of_nodes):
        for col in range(num_of_nodes):
            if row == col:
                distance = np.inf
            else:
                x_1, y_1 = nodes[row]
                x_2, y_2 = nodes[col]
                distance = np.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) 
            d_matrix[row, col] = distance
    return d_matrix