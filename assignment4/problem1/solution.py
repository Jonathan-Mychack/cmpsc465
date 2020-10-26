# Name: Jonathan Mychack
# Course: CMPSC 465
# Date Last Modified: 10/25/20
# Assignment 4, Problem 1

def Bellman_Ford(graph, distance, previous):
    for k in range(1, len(graph)):
        for u, v, l in graph:
            if dist[v-1] > dist[u-1] + l:
                dist[v-1] = dist[u-1] + l
                prev[v-1] = u
    for u, v, l in graph:  #additional iteration to determine if there is a negative cycle
        if dist[v-1] > dist[u-1] + l:
            return True
    return False

info = list(map(int, input().split(" ")))  #[num vertices, num edges, source vertex]

dist = []
prev = []
for i in range(info[0]):
    dist.append(1001)  #1000 is the maximum length of an edge, so 1001 represents infinity
    prev.append(None)  #initialize all previous vertices to null/none

graph = []

for i in range(info[1]):  #construct the adjacency list
    edge = list(map(int, input().split(" "))) # edge = [source, destination, length]
    graph.append([edge[0], edge[1], edge[2]])
    if info[2]-1 == i:
        dist[i] = 0

print(Bellman_Ford(graph, dist, prev))
