from utils import generate_nodes, create_distance_matrix
from algorithms import nearest_neighbour, held_karp
from visuals import plot_path
from performance import get_aggregate_stats

AMOUNT_OF_NODES = 10
MAP_LENGTH = 50

def main():
    nodes = generate_nodes(AMOUNT_OF_NODES, MAP_LENGTH)
    d_matrix = create_distance_matrix(nodes)
    #path, distance = nearest_neighbour(d_matrix)
    #plot_path(nodes, path, MAP_LENGTH)
    #path, distance = held_karp(d_matrix)
    #plot_path(nodes, path, MAP_LENGTH)
    get_aggregate_stats(AMOUNT_OF_NODES, MAP_LENGTH, 10, 201, 20, nearest_neighbour)
    get_aggregate_stats(AMOUNT_OF_NODES, MAP_LENGTH, 10, 201, 20, held_karp)

if __name__ == "__main__":
    main()