# -*- coding: utf-8 -*-
# Array
"""
Created on Tue Jan 24 12:01:22 2023

@author: Ahlam
"""
# -*- coding: utf-8 -*-
# Floyd-Warshall Algorithm in python

import numpy as np
nV = 23
INF = 999

# Algorithm implementation
def floyd_warshall(G):
    distance =  np.array(G)
    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    # print_solution(nV,distance)
    
# Printing the solution
def print_solution(nV,distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

# graph = np.array([ [0,3,INF,7],[8,0,2,INF],[5,INF,0,1],[2,INF,INF,0] ])
# floyd_warshall(4,graph)


