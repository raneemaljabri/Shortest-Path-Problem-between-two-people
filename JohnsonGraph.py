# -*- coding: utf-8 -*-
# Graph
"""
Created on Tue Jan 24 12:01:22 2023

@author: Ghydaa
"""
# -*- coding: utf-8 -*-
# Johnson's Algorithm in python

class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
    def __contains__(self, key):
        return key in self.vertices
    def add_edge(self, src_key, dest_key, weight):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
    def __len__(self):
        return len(self.vertices)
    def __iter__(self):
        return iter(self.vertices.values())
 #Class for vertex
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
    def set_weight(self, dest, weight):
        """Set weight of edge from this vertex to dest."""
        self.points_to[dest] = weight
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
def johnson(g):
    """Return distance is the shortest distance from vertex u to v.
    g is a Graph object which can have negative edge weights """

#*****I just skkiped this step bc there isn't any negative weight or edge.*****
    # compute shortest distance from vertex q to all other vertices
    # set weight(u, v) = weight(u, v) + bell_dist(u) - bell_dist(v) for each
    # edge (u, v)
    # remove vertex q
    # This implementation of the graph stores edge (u, v) in Vertex object u
    # Since no other vertex points back to q, we do not need to worry about
    # removing edges pointing to q from other vertices.
    # distance[u][v] will hold smallest distance from vertex u to v
    # distance = {}
    # run dijkstra's algorithm on each source vertex
    # print ("run dijkstra's algorithm on each source vertex")
    # for v in g:
    #     distance[v] = dijkstra(g, v)
    #     for k in g:
    #         print('Shortest distance from {} to {} is '.format(v.get_key(), k.get_key()), end=' ')
    #         print('{}'.format(distance[v][k]))
    # return distance

def bellman_ford(g, source):
    """Return distance where This will return a dictionary distance.
       g is a Graph object which can have negative edge weights."""
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0
    for _ in range(len(g) - 1):
        for v in g:
            for n in v.get_neighbours():
                distance[n] = min(distance[n], distance[v] + v.get_weight(n))
    return distance

def dijkstra(g, source):
    #Return shortest distance after ensure that there is no negative weight
    unvisited = set(g)
    distance = dict.fromkeys(g, float('inf'))
    distance[source] = 0
    while unvisited != set():
        # find vertex with minimum distance
        closest = min(unvisited, key=lambda v: distance[v])
        # mark as visited
        unvisited.remove(closest)
        # update distances
        for neighbour in closest.get_neighbours():
           if neighbour in unvisited:
               new_distance = distance[closest] + closest.get_weight(neighbour)
               if distance[neighbour] > new_distance:
                   distance[neighbour] = new_distance
    return distance

# g = Graph()
# # print('Graph')
# for x in range(1, 5001):
#     g.add_vertex(x)
# with open("Raneem.txt") as file:
#     for line in file:
#         g.add_edge(int(line.rstrip().split()[0]), int(line.rstrip().split()[1]), float(line.rstrip().split()[2]))
# distance = johnson(g)
# print('Shortest distances:')
# for start in g:
#     for end in g:
#         print('{} to {}'.format(start.get_key(), end.get_key()), end=' ')
#         print('distance {}'.format(distance[start][end]))

