# An Invesitigation of the Travelling Salesman Problem

## Overview

This project will be an exploration and comparison of different methods used to solve or attempt to solve, the travelling salesman problem (TSP). The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits each city exactly once and then returns to the starting city. This project will compare the nearest neighbour algorithm, Held-Karp algorithm, simulated annealing, and (maybe) ant colony optimization.

## Nearest Neighbour Algorithm

This algorithm chooses the closest city as the next one to visit until every city has been visited and then returns to the starting city.

### To Do
- impliment the four algos
- write some basic tests like:
    - path starts and ends with same node
    - no duplicate nodes in paths
    - make a non random graph and make sure distance is as expected
    - maybe see what happens when there are 3 nodes (the min allowed)