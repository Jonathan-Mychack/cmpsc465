# Name: Jonathan Mychack
# Course: CMPSC 462
# Date Last Accessed: 10/8/20
# Assignment 3, Problem 1

def dfs(graph):
    num_cc = 0
    for i in range(len(graph)):
        

def explore(graph, vertex):  #for the way we parse inputs, graph is adj_list and vertex is the index in adj_list


num = list(map(int, input().split(" "))) # num = [num vertices, num edges]
adj_list = []

for i in range(num[0]):  #insert the number of elements needed into the adjacency list
    adj_list.append([]) #after the for loop, adj_list looks like [[], [], [], ...]

for i in range(num[1]):  #construct the adjacency list
    edge = list(map(int, input().split(" "))) # edge = [source, destination]
    adj_list[edge[0]-1].append(edge[1]) #0th elem is vertex 1, 1st elem is vertex 2, etc
