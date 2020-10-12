# Name: Jonathan Mychack
# Course: CMPSC 462
# Date Last Accessed: 10/12/20
# Assignment 3, Problem 1

def dfs(graph, visited_cc, order):
    num_cc = 0
    for i in range(len(order)):
        for j in range(len(graph[order[i]-1])):
            if visited_cc[order[i]-1] == 0:
                num_cc += 1
                explore(graph, graph[order[i]-1][j]-1, visited_cc, num_cc)

def explore(graph, vertex, visited_cc, num_cc): #for the way we parse inputs, graph is adj_list and vertex is the index in adj_list
    visited_cc[vertex] = num_cc
    for i in range(len(graph[vertex])):
        if visited_cc[graph[vertex][i]-1] == 0:
            explore(graph, graph[vertex][i]-1, visited_cc, num_cc)

def dfs_with_timing(graph, visited, pre, post, postlist):
    clk = 1
    for i in range(len(graph)):
        if visited[i] == 0:
            explore_with_timing(graph, i, visited, pre, post, postlist, clk)

def explore_with_timing(graph, vertex, visited, pre, post, postlist, clk):
    visited[vertex] = 1
    pre[vertex] = clk
    clk += 1
    for i in range(len(graph[vertex])):
        if visited[graph[vertex][i]-1] == 0:
            explore_with_timing(graph, graph[vertex][i]-1, visited, pre, post, postlist, clk)
    post[vertex] = clk
    clk += 1
    postlist.append(vertex+1)

def get_specific_order(graph):
    reverse_graph = []

    for i in range(len(graph)):  #insert the same amount of elements from graph into the reverse
        reverse_graph.append([])

    for i in range(len(graph)):  #invert all of the edges, looks like O(n^2) but it's actually O(|V|+|E|)
        for j in range(len(graph[i])):
            reverse_graph[int(graph[i][j])-1].append(i+1)
    
    return reverse_graph
    

num = list(map(int, input().split(" "))) # num = [num vertices, num edges]
adj_list = []

for i in range(num[0]):  #insert the number of elements needed into the adjacency list
    adj_list.append([]) #after the for loop, adj_list looks like [[], [], [], ...]

for i in range(num[1]):  #construct the adjacency list
    edge = list(map(int, input().split(" "))) # edge = [source, destination]
    adj_list[edge[0]-1].append(edge[1]) #0th elem is vertex 1, 1st elem is vertex 2, etc

visited = []
visited_cc = []
pre = []
post = []
postlist = []
for i in range(len(adj_list)):
    visited.append(0)
    visited_cc.append(0)
    pre.append(0)
    post.append(0)

reverse_graph = get_specific_order(adj_list)
dfs_with_timing(reverse_graph, visited, pre, post, postlist)
specific_order = postlist[::-1]
dfs(adj_list, visited_cc, specific_order)
print(visited_cc)
max = 0
for i in range(len(visited_cc)):
    if visited_cc[i] > max:
        max = visited_cc[i]

print(max)