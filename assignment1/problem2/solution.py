# Name: Jonathan Mychack
# Date Last Accessed: 8/31/20
# Course: CMPSC 465
# Assignment 1, Problem 2

def merge_two_sorted_arrays(array1, array2): #slightly modified code from problem1 to account for the change in array format
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
            if array1[size_count1] <= array2[size_count2]:
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


size = int(input())
array = list(map(int, input().split(" ")))
result = merge_sort(size, array)
for i in range(size):
    if i == size - 1:
        print(result[i])
    else:
        print(result[i], end = " ")
