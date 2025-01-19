from collections import namedtuple
import random
import matplotlib.pyplot as plt
import numpy as np

# For printing the plt visual on second monitor
manager = plt.get_current_fig_manager()
tk_window = manager.canvas.manager.window
x_offset = 2500
y_offset = 100
tk_window.geometry(f"+{x_offset}+{y_offset}")

AMOUNT_OF_NODES = 10
MAP_LENGTH = 50

def generate_nodes(amount, map_length):
    ''' Generates unique randomly positioned nodes '''
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

def nearest_neighbor(d_matrix, start_node=0):
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

        for node_idx in range(1, number_of_nodes):
            if not visited[node_idx] and d_matrix[current_node, node_idx] < nearest_distance:
                nearest_distance = d_matrix[current_node, node_idx]
                nearest_node = node_idx
        
        path.append(nearest_node)
        visited[nearest_node] = True
        total_distance += nearest_distance
        current_node = nearest_node

    # Return to starting node
    path.append(0)

    return path, total_distance

def plot_path(nodes, path):
    ''' Plot the nodes and the path '''
    x_values, y_values = zip(*nodes)
    plt.scatter(x_values, y_values)

    previous_node = path[0]
    for node in path[1:]:
        x_1, y_1 = nodes[previous_node]
        x_2, y_2 = nodes[node]
        plt.plot([x_1, x_2], [y_1, y_2])
        previous_node = node

    plt.show()

def main():
    sims = range(10, 5001, 20)
    avgs = []
    mins = []
    maxs = []
    for sim in sims:
        distances = []
        for _ in range(sim):
            nodes = generate_nodes(AMOUNT_OF_NODES, MAP_LENGTH)
            d_matrix = create_distance_matrix(nodes)
            path, total_distance = nearest_neighbor(d_matrix)
            distances.append(total_distance)
        mean = np.mean(distances)
        avgs.append(mean)
        mins.append(min(distances))
        maxs.append(max(distances))
        print(mean)
    plt.ylim(0, max(avgs)*2)
    plt.plot(sims, avgs, c='blue')
    plt.plot(sims, mins, c='green')
    plt.plot(sims, maxs, c='red')
    plt.show()
    #plot_path(nodes, path)

if __name__ == "__main__":
    main()