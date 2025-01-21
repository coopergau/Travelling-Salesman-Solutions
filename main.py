from utils import generate_nodes, create_distance_matrix
from algorithms import nearest_neighbour
from visuals import plot_path

AMOUNT_OF_NODES = 10
MAP_LENGTH = 50

def main():
    nodes = generate_nodes(AMOUNT_OF_NODES, MAP_LENGTH)
    d_matrix = create_distance_matrix(nodes)
    path, total_distance = nearest_neighbour(d_matrix)
    plot_path(nodes, path, MAP_LENGTH)
    #get_aggregate_stats(10, 2001, 20)

if __name__ == "__main__":
    main()