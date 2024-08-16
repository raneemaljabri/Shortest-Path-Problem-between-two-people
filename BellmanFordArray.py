# -*- coding: utf-8 -*-
# Array
"""
Created on Tue Jan 24 12:01:22 2023

@author: Raneem
"""
# -*- coding: utf-8 -*-
# Bellman-Ford Algorithm in python

import sys
def bellmanford(garph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]}
    }
    node_data[src]['cost'] = 0
    for i in range(5):
        print('Iteration '+str(i))
        for itr in garph:
            for neighbor in garph[itr]:
                cost = node_data[itr]['cost'] + garph[itr][neighbor]
                if cost < node_data[neighbor]['cost']:
                    node_data[neighbor]['cost'] = cost
                    if node_data[neighbor]['cost'] == inf:
                        node_data[neighbor]['pred'] = node_data[itr]['pred'] + [itr]
                    else:
                        node_data[neighbor]['pred'].clear()
                        node_data[neighbor]['pred'] = node_data[itr]['pred'] + [itr]
        print(node_data)
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred']))

# if __name__ == "__main__":
#     garph = {
#         'A':{'B':6,'C':4,'D':5},
#         'B':{'E':-1},
#         'C':{'B':-2,'E':3},
#         'D':{'C':-2,'F':-1},
#         'E':{'F':3},
#         'F':{}
#     }

#     source = 'A'
#     destination = 'E'
#     bellmanford(garph,source,destination)

