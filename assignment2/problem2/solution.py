# Name: Jonathan Mychack
# Date Last Accessed: 9/20/20
# Course: CMPSC 465
# Assignment 2, Problem 2

import math

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        return self.top == None

    def __len__(self):
        return self.count

    def peek(self):
        if len(self) == 0:
            return 'Stack is empty'
        return self.top.value

    def push(self,value):
        newNode = Node(value)
        if self.isEmpty() is True:  #set self.top equal to value if list is empty
            self.top = newNode
        else:  #make current self.top next in the stack and make newNode the top
            newNode.next = self.top
            self.top = newNode
        self.count += 1

    def pop(self):
        if self.isEmpty() is True:  #return error if stack is empty
            return 'Stack is empty'
        else:  #return and delete value of self.top; make the next value the new top
            temp = self.top
            self.top = self.top.next
            self.count -= 1
            return temp.value


def merge_two_sorted_arrays(pstar, array1, array2):
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
            if find_angle(pstar, array1[size_count1]) <= find_angle(pstar, array2[size_count2]):
                output_array.append(array1[size_count1])
                size_count1 += 1
            else:
                output_array.append(array2[size_count2])
                size_count2 += 1
        if size_count1 == len(array1) and size_count2 == len(array2):
            return output_array


def merge_sort(pstar, size, array):
    if size <= 1:
        return array
    
    if size % 2 == 0:
        first_half = merge_sort(pstar, size/2, array[:int(size/2)])
        second_half = merge_sort(pstar, size/2, array[int(size/2):])
    else:
        first_half = merge_sort(pstar, (size/2) - 0.5, array[:int((size/2) - 0.5)])
        second_half = merge_sort(pstar, (size/2) + 0.5, array[int((size/2) - 0.5):])
    result = merge_two_sorted_arrays(pstar, first_half, second_half)
    return result

def find_angle(pstar, point):
    vector = [point[0] - pstar[0], point[1] - pstar[1]]
    if vector[1] == 0:
        if (vector[0] < 0):
            return 180
        elif (vector[0] >= 0):
            return 0
    magnitude = math.sqrt((vector[0] ** 2) + (vector[1] ** 2))
    normal = [vector[0] / magnitude, vector[1] / magnitude]
    angle = math.acos(normal[0])
    return angle

def check_orientation(pstar, point1, point2):
    vector1 = [pstar[0] - point1[0], pstar[1] - point1[1]]
    vector2 = [point1[0] - point2[0], point1[1] - point2[1]]
    if ((vector1[0] * vector2[1]) - (vector1[1] * vector2[0])) > 0:
        return 'turning left'
    elif ((vector1[0] * vector2[1]) - (vector1[1] * vector2[0])) < 0:
        return 'turning right'
    else:
        return 'colinear'


def graham_scan(points):
    smallest_coord = [-1, 101]      # [index, value]
    for i in range(len(points)):
        if points[i][1] < smallest_coord[1]:
            smallest_coord[0] = i
            smallest_coord[1] = points[i][1]
    p_star = points[smallest_coord[0]]
    sorted_array = merge_sort(p_star, len(points), points)
    return graham_scan_core(sorted_array)


def graham_scan_core(points):
    s = Stack()
    s.push(points[0])
    s.push(points[1])
    s.push(points[2])
    for k in range(3, len(points)):
        while s.isEmpty() == False:
            if len(s) < 3:
                break
            pa = s.top.value
            pb = s.top.next.value
            if check_orientation(points[0], pa, pb) == 'turning right':
                s.pop()
                continue
            elif check_orientation(points[0], pa, pb) == 'turning left':
                break
        s.push(points[k])
    return len(s)

            
point_array = []
point_array_dual = []
for i in range(int(input())):
    line = list(map(float, input().split(" ")))
    line[1] *= -1
    point_array.append(line)
    line[0] *= -1
    line[0] *= -1
    point_array_dual.append(line)
half = graham_scan(point_array)
other = graham_scan(point_array_dual)
print(half, other)
