# -*- coding: utf-8 -*-
#Dijkstra's & Bellman-Ford & Floyd-Warshall & Johnson's Algorithms
"""
Created on Tue Jan 24 12:01:22 2023

@author: Mawaddah & Maani & Raneem & Ahlam & Ghydaa
"""
# -*- coding: utf-8 -*-
# Shortest Path Problem in python

#https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
#https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/

import DijkstraAdjacencyList
import DijkstraPriorityQueue
import BellmanFordArray
import BellmanFordLinkedList
import FloydWarshallArray
import FloydWarshallList
import FloydWarshallDequeue
import JohnsonGraph
import JohnsonStack
import timeit

def readFile():
    my_file = open("Raneem.txt", "r")
    nums = my_file.readlines()
    nums = [list(i) for i in nums]
    return nums

numbers = readFile()
size = len(numbers)

def menu():
    ch = int(input("Choose a number from the following"
        + "Shortest Path Problem menu: "
        + "\n1. Dijkstra's Algorithm. "
        + "\n2. Bellman-Ford Algorithm. "
        + "\n3. Floyd-Warshall Algorithm. "
        + "\n4. Johnson's Algorithm. " 
        + "\n5. Exit.\n"))
    return ch

def menu1():
        ch1 = int(input("Choose a number from the following" 
            + "Dijkstra's Algorithm menu: "
            + "\n1. Adjacency List Data Structure. "
            + "\n2. Priority Queue Data Structure. "
            + "\n3. Exit.\n"))
        return ch1
    
# Adjacency List Data
graph = DijkstraAdjacencyList.Graph(17)
graph.addEdge(0, 0, 0)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(1, 8, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(2, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(3, 8, 10)
graph.addEdge(3, 6, 2)
graph.addEdge(4, 3, 6)
graph.addEdge(4, 8, 7)
graph.addEdge(4, 9, 11)
graph.addEdge(5, 1, 7)
graph.addEdge(5, 9, 2)
graph.addEdge(5, 11, 11)
graph.addEdge(6, 0, 5)
graph.addEdge(6, 3, 3)
graph.addEdge(6, 8, 4)
graph.addEdge(7, 1, 2)
graph.addEdge(7, 11, 10)
graph.addEdge(7, 2, 3)
graph.addEdge(8, 8, 7)
graph.addEdge(8, 2, 17)
graph.addEdge(8, 10, 2)
graph.addEdge(9, 1, 1)
graph.addEdge(9, 2, 6)
graph.addEdge(9, 3, 7)
graph.addEdge(10, 4, 4)
graph.addEdge(10, 5, 8)
graph.addEdge(10, 6, 1)
graph.addEdge(11, 7, 19)
graph.addEdge(11, 8, 1)
graph.addEdge(11, 9, 2)
graph.addEdge(11,10, 9)
graph.addEdge(12, 11, 11)
graph.addEdge(12, 12, 2)
graph.addEdge(12, 13, 4)
graph.addEdge(13, 14, 6)
graph.addEdge(13, 15, 8)
graph.addEdge(13, 1, 10)
graph.addEdge(14, 16, 1)
graph.addEdge(14, 3, 3)
graph.addEdge(14, 8, 5)
graph.addEdge(15, 9, 7)
graph.addEdge(15, 0, 9)
graph.addEdge(15, 2, 11)
graph.addEdge(15, 1, 13)
graph.addEdge(16, 6, 7)

# Priority Queue Data
G = { # random example graph
  'A': {('C', 76)}, 
  'B': {('C', 20), ('J', 78)}, 
  'C': {('C', 62), ('F', 99), ('G', 72), ('H', 40)}, 
  'D': {('A',  8), ('G', 71), ('I', 61)}, 
  'E': {('C', 16), ('E', 54), ('I',  3)}, 
  'F': {('J', 66)}, 
  'G': {('B', 92), ('E', 48), ('G', 31)}, 
  'H': {('G', 36)}, 
  'I': {('J', 88), ('K', 16)}, 
  'J': {('H',  4), ('K', 46)}, 
  'K': {('I', 40)} 
}

def menu2():
        ch2 = int(input("Choose a number from the following"
            + "Bellman-Ford Algorithm menu: "
            + "\n1. Array Data Structure. "
            + "\n2. Linked List Data Structure. "
            + "\n3. Exit.\n"))
        return ch2

# Array Data
if __name__ == "__main__":
    garph = {
        'A':{'B':6,'C':4,'D':5},
        'B':{'E':-1},
        'C':{'B':-2,'E':3},
        'D':{'C':-2,'F':-1},
        'E':{'F':3},
        'F':{}
    }
    source = 'A'
    destination = 'E'

# Linked List Data
g = BellmanFordLinkedList.Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 2)
g.add_edge(2, 4, 3)
g.add_edge(2, 3, 4)
g.add_edge(4, 3, -5)

def menu3():
        ch3 = int(input("Choose a number from the following" 
            + "Floyd-Warshall Algorithm menu: "
            + "\n1. Array Data Structure. "
            + "\n2. List Data Structure. "
            + "\n3. Data Structure. "
            + "\n4. Exit.\n"))
        return ch3

def menu4():
        ch4 = int(input("Choose a number from the following"
            + "Johnson's Algorithm menu: "
            + "\n1. Graph Data Structure. "
            + "\n2. Stack Data Structure. "
            + "\n3. Exit.\n"))
        return ch4

# Stack Data
srcStack = []
desStack = []
weightStack = []
with open("Raneem.txt") as file:
    for line in file:
        srcStack.append(line.rstrip().split()[0])
        desStack.append(line.rstrip().split()[1])
        weightStack.append(float(line.rstrip().split()[2]))
g = JohnsonStack.Graph()
for x in range(1, 5001):
    g.add_vertex(x)#add all data

with open("Raneem.txt") as file:#read the file
    for line in file:
        g.add_edge(int(srcStack.pop()), int(desStack.pop()), weightStack.pop())#Pop the data from stack

# Graph Data
g = JohnsonGraph.Graph()
for x in range(1, 5001):
    g.add_vertex(x)
with open("Raneem.txt") as file:
    for line in file:
        g.add_edge(int(line.rstrip().split()[0]), int(line.rstrip().split()[1]), float(line.rstrip().split()[2]))

def dijkstraMenu():
    loop1 = True
    while(loop1): 
        choice1 = menu1() 
        #check what choice was entered and act accordingly
        if(choice1 == 1): 
            str1 = timeit.default_timer()
            graph.dijkstra(0)
            end1 = timeit.default_timer()
            tim1 = end1 - str1
            print("The Dijkstra's Adjacency List time is: ", tim1)
            continue
        elif(choice1 == 2):
            str2 = timeit.default_timer()
            parent = DijkstraPriorityQueue.dijkstra(G, 'A', 'K')
            end2 = timeit.default_timer()
            tim2 = end2 - str2
            print(DijkstraPriorityQueue.make_path(parent, 'K'))
            print("The Dijkstra's Priority Queue time is: ", tim2)
            continue 
        elif(choice1 == 3):
            loop1 = False
            break
        else:
            print("Invalid choice")
            continue
        
def bellmanFordMenu():
    loop2 = True
    while(loop2): 
        choice2 = menu2() 
        #check what choice was entered and act accordingly
        if(choice2 == 1): 
            str1 = timeit.default_timer()
            BellmanFordArray.bellmanford(garph,source,destination)
            end1 = timeit.default_timer()
            tim1 = end1 - str1
            print("The Bellman-Ford Array time is: ", tim1)
            continue
        elif(choice2 == 2):
            str2 = timeit.default_timer()
            g.bellman_ford(0)
            end2 = timeit.default_timer()
            tim2 = end2 - str2
            print("The Bellman-Ford Linked List time is: ", tim2)
            continue
        elif(choice2 == 3):
            loop2 = False
            break
        else:
            print("Invalid choice")
            continue
        
def floydWarshallMenu():
    loop3 = True
    while(loop3): 
        choice3 = menu3() 
        #check what choice was entered and act accordingly
        if(choice3 == 1): 
            str1 = timeit.default_timer()
            FloydWarshallArray.floyd_warshall(numbers)
            end1 = timeit.default_timer() 
            tim1 = end1 - str1
            print("The Floyd-Warshall Array time is: ", tim1)
            continue
        elif(choice3 == 2):
            str2 = timeit.default_timer()
            FloydWarshallList.floyd_warshall(numbers)
            end2 = timeit.default_timer()
            tim2 = end2 - str2
            print("The Floyd-Warshall List time is: ", tim2)
            continue
        elif(choice3 == 3):
            str3 = timeit.default_timer()
            FloydWarshallDequeue.floyd_warshall(numbers)
            end3 = timeit.default_timer()
            tim3 = end3 - str3
            print("The Floyd-Warshall Dequeue time is: ", tim3)
            continue
        elif(choice3 == 4):
            loop3 = False
            break
        else:
            print("Invalid choice")
            continue
def johnsonMenu():
    loop4 = True
    while(loop4): 
        choice4 = menu4() 
        #check what choice was entered and act accordingly
        if(choice4 == 1): 
            str1 = timeit.default_timer()
            JohnsonGraph.johnson(g)
            end1 = timeit.default_timer()
            tim1 = end1 - str1
            print("The Johnson's Algorithm Graph time is: ", tim1)
            continue
        elif(choice4 == 2):
            str2 = timeit.default_timer()
            JohnsonStack.johnson(g)
            end2 = timeit.default_timer()
            tim2 = end2 - str2
            print("The Johnson's Algorithm Stack time is: ", tim2)
            continue
        elif(choice4 == 3):
            loop4 = False
            break
        else:
            print("Invalid choice")
            continue
    
#Shortest Path Problem Menu
loop = True
while(loop): 
    choice = menu() 
    #check what choice was entered and act accordingly
    if(choice == 1): 
        dijkstraMenu()
        continue
    elif(choice == 2):
        bellmanFordMenu()
        continue
    elif(choice == 3):
        floydWarshallMenu()
        continue
    elif(choice == 4):
        johnsonMenu()
        continue 
    elif(choice == 5):
        loop = False
        break
    else:
        print("Invalid choice")
        continue
    