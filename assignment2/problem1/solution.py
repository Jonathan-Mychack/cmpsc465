# Name: Jonathan Mychack
# Date Last Accessed: 9/16/20
# Course: CMPSC 465
# Assignment 2, Problem 1

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
        return 0
    
    if size % 2 == 0:
        first_half = merge_sort(size/2, array[:int(size/2)])
        second_half = merge_sort(size/2, array[int(size/2):])
    else:
        first_half = merge_sort((size/2) - 0.5, array[:int((size/2) - 0.5)])
        second_half = merge_sort((size/2) + 0.5, array[int((size/2) - 0.5):])
    result_array, result_count = merge_and_count(first_half, second_half)
    return result_count

def merge_and_count(array1, array2):
    output_array = []
    pointer1 = 0
    pointer2 = 0
    count = 0
    while ((len(array1) > 0) and (len(array2) > 0)):
        element1 = array1[pointer1]
        element2 = array2[pointer2]
        if element1 <= element2:
            output_array.append(element1)
            count += (len(array1) - pointer1)
            pointer1 += 1
        else:
            output_array.append(element2)
            count += (len(array2) - pointer2)
            pointer2 += 1
    if len(array1) == 0:
        for i in range(pointer2, len(array2)):
            output_array.append(array2[i])
            return output_array, count
    elif len(array2) == 0:
        for i in range(pointer1, len(array1)):
            output_array.append(array1[i])
            return output_array, count

size = int(input())
array = list(map(int, input().split(" ")))
result = merge_sort(size, array)
print(result)