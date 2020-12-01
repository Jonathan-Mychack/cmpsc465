# Name: Jonathan Mychack
# Course: CMPSC 465
# Date Last Accessed: 11/30
# Assignment 5, Problem 2

class Node:

    def __init__(self):
        self.data = None
        self.height = 0
        self.parent = None

    def make_set(self):
        self.height = 1
        self.parent = self

    def find(self, node):
        while node.parent != node:
            node = node.parent
        return(node)

    def union(self, x, y):
        rx = x.find(x)
        ry = y.find(y)
        if rx == ry:
            return
        if rx.height < ry.height:
            rx.parent = ry
        elif rx.height > ry.height:
            ry.parent = rx
        else:
            rx.parent = ry
            ry.height += 1


def kruskals(adj_list, edges, nodes, mst):
    for i in range(1, len(adj_list)):
        nodes[i].make_set()
    for i in range(len(edges)):
        outgoing_vertex = edges[i][0]
        ru = nodes[outgoing_vertex].find(nodes[outgoing_vertex])
        incoming_vertex = edges[i][1]
        rv = nodes[incoming_vertex].find(nodes[incoming_vertex])
        if ru != rv:
            mst.append(edges[i][2])
            nodes[outgoing_vertex].union(ru, rv)


def merge_two_sorted_arrays(array1, array2):
    output_array = []
    size_count1 = 0
    size_count2 = 0
    for i in range(0, len(array1) + len(array2)):
        if size_count1 < len(array1) and size_count2 >= len(array2):
            output_array.append(array1[size_count1])
            size_count1 += 1
        elif size_count1 >= len(array1) and size_count2 < len(array2):
            output_array.append(array2[size_count2])
            size_count2 += 1
        else:
            if array1[size_count1][2] <= array2[size_count2][2]:
                output_array.append(array1[size_count1])
                size_count1 += 1
            else:
                output_array.append(array2[size_count2])
                size_count2 += 1
        if size_count1 == len(array1) and size_count2 == len(array2):
            return output_array


def merge_sort(size, array):
    if size <= 1:
        return array
    
    if size % 2 == 0:
        first_half = merge_sort(size/2, array[:int(size/2)])
        second_half = merge_sort(size/2, array[int(size/2):])
    else:
        first_half = merge_sort((size/2) - 0.5, array[:int((size/2) - 0.5)])
        second_half = merge_sort((size/2) + 0.5, array[int((size/2) - 0.5):])
    result = merge_two_sorted_arrays(first_half, second_half)
    return result

num_vert_edge = list(map(int, input().split(" ")))
adj_list = [[]]
edges = []
mst = []

for i in range(num_vert_edge[0]):
    adj_list.append([])

for i in range(num_vert_edge[1]):
    edges.append(list(map(int, input().split(" "))))
    adj_list[edges[i][0]].append(edges[i][1])
    adj_list[edges[i][0]].append(edges[i][2])

sorted_edges = merge_sort(len(edges), edges)
node_vertices = [[]]
for i in range(num_vert_edge[0]):
    node_vertices.append(Node())

kruskals(adj_list, sorted_edges, node_vertices, mst)
count = 0
for i in range(len(mst)):
    count += mst[i]

print(count)