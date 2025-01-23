from utils import generate_nodes, create_distance_matrix
import numpy as np
import matplotlib.pyplot as plt

# Maybe rework or reorganize this ---------------------------------------------------------------------------

def get_aggregate_stats(amount_of_nodes, map_length, min_sims, max_sims, step_size, solving_function):
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
            nodes = generate_nodes(amount_of_nodes, map_length)
            d_matrix = create_distance_matrix(nodes)
            path, total_distance = solving_function(d_matrix)
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
