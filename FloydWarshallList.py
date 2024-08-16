# -*- coding: utf-8 -*-
# List
"""
Created on Tue Jan 24 12:01:22 2023

@author: Ahlam
"""
# -*- coding: utf-8 -*-
# Floyd-Warshall Algorithm in python

nV = 23
INF = 999

# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    # print_solution(distance)

# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

# G = [[0, 3, INF, 7],
#     [8, 0, 2,INF],
#     [5, INF, 0, 1],
#     [2, INF, INF, 0]]
# floyd_warshall(G)


