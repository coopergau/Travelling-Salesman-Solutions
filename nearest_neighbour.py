from collections import namedtuple
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    
    # Create the figure and axis
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)

    # Create an empty line object that will be updated during the animation
    line, = ax.plot([], [], 'g-', lw=2)

    ax.set_xlim(0, MAP_LENGTH)
    ax.set_ylim(0, MAP_LENGTH)

    # Line initialization function
    def init():
        line.set_data([], [])
        return (line,)  

    # Update function to draw each new line
    def update(frame):
        # Get the x and y coordinates for the path up to the current frame
        path_x = [x_values[i] for i in path[:frame+1]]
        path_y = [y_values[i] for i in path[:frame+1]]
        
        # Update the line with the new path data
        line.set_data(path_x, path_y)
        return (line,)

    # Animate the path
    ani = FuncAnimation(fig, update, frames=len(path), init_func=init, blit=True, interval=200)

    plt.show()
    
def get_aggregate_stats(min_sims, max_sims, step_size):
    ''' Function starts by running min_sims simulations of the algorithm and records the total distances
        of each, calculating the min, max and mean. It then increases the number of sims by step_size and
        repeats the process until max_sims is reached (not included). The function then plots a distance vs.
        number of sims graph with lines for min, max and mean. '''
    sims = range(min_sims, max_sims, step_size)
    mins = []
    maxs = []
    means = []
    for sim in sims:
        distances = []
        for _ in range(sim):
            nodes = generate_nodes(AMOUNT_OF_NODES, MAP_LENGTH)
            d_matrix = create_distance_matrix(nodes)
            path, total_distance = nearest_neighbor(d_matrix)
            distances.append(total_distance)
        mins.append(min(distances))
        maxs.append(max(distances))
        mean = np.mean(distances)
        means.append(mean)
        print(mean)
    plt.ylim(0, max(means)*2)
    plt.plot(sims, mins, c='green')
    plt.plot(sims, maxs, c='red')
    plt.plot(sims, means, c='blue')
    plt.show()

def main():
    nodes = generate_nodes(AMOUNT_OF_NODES, MAP_LENGTH)
    d_matrix = create_distance_matrix(nodes)
    path, total_distance = nearest_neighbor(d_matrix)
    plot_path(nodes, path)
    #get_aggregate_stats(10, 2001, 20)

if __name__ == "__main__":
    main()