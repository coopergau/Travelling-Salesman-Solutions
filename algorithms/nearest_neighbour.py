import numpy as np

def nearest_neighbour(d_matrix, start_node=0):
    ''' The nearest neighbour algorithm '''
    number_of_nodes = len(d_matrix)
    visited = [False] * number_of_nodes 
    path = [start_node]
    total_distance = 0
    current_node = start_node
    visited[current_node] = True

    for _ in range(number_of_nodes - 1):
        nearest_distance = np.inf
        nearest_node = None

        # Starting at the first node, find the closest unvisited node
        for node_idx in range(1, number_of_nodes):
            if not visited[node_idx] and d_matrix[current_node, node_idx] < nearest_distance:
                nearest_distance = d_matrix[current_node, node_idx]
                nearest_node = node_idx
        
        # Add that node to the path list and set it as the current position
        path.append(nearest_node)
        visited[nearest_node] = True
        total_distance += nearest_distance
        current_node = nearest_node
        
    # Return to starting node
    path.append(0)
    return path, total_distance