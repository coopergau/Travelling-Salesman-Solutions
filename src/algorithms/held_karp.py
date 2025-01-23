import numpy as np
import itertools

# This code is from this medium article: https://medium.com/@davidlfliang/intro-python-algorithms-traveling-salesman-problem-ffa61f0bd47b
# The focus of this project is on the other methods, but it is useful to have a method that finds an exact solution to compare to.

def held_karp(d_matrix):
    ''' The Held-Karp algorithm '''
    number_of_nodes = len(d_matrix)

    dp = [[np.inf] * number_of_nodes for _ in range(1 << number_of_nodes)]
    parent = [[None] * number_of_nodes for _ in range(1 << number_of_nodes)]

    # Base case: starting from city 0
    dp[1][0] = 0

    # Fill DP table
    for mask in range(1 << number_of_nodes):
        for last in range(number_of_nodes):
            if not (mask & (1 << last)):
                continue
            for next in range(number_of_nodes):
                if mask & (1 << next):
                    continue
                new_mask = mask | (1 << next)
                new_dist = dp[mask][last] + d_matrix[last][next]
                if new_dist < dp[new_mask][next]:
                    dp[new_mask][next] = new_dist
                    parent[new_mask][next] = last

    # Find the optimal path and minimum cost
    min_cost = np.inf
    end_city = None
    full_mask = (1 << number_of_nodes) - 1

    for last in range(1, number_of_nodes):
        cost = dp[full_mask][last] + d_matrix[last][0]
        if cost < min_cost:
            min_cost = cost
            end_city = last

    # Reconstruct the optimal path
    path = []
    mask = full_mask
    last = end_city
    while mask:
        path.append(last)
        new_last = parent[mask][last]
        mask ^= (1 << last)
        last = new_last
    path = path[::-1]
    path.append(0)  # Add the starting city at the end to complete the loop

    return path, min_cost