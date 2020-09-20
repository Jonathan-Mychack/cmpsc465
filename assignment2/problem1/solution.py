# Name: Jonathan Mychack
# Date Last Accessed: 9/16/20
# Course: CMPSC 465
# Assignment 2, Problem 1

def merge_sort(size, array):
    if size <= 1:
        return array, 0

    count = 0

    if size % 2 == 0:
        first_half, first_count = merge_sort(size/2, array[:int(size/2)])
        second_half, second_count = merge_sort(size/2, array[int(size/2):])
        count += first_count + second_count
    else:
        first_half, first_count = merge_sort((size/2) - 0.5, array[:int((size/2) - 0.5)])
        second_half, second_count = merge_sort((size/2) + 0.5, array[int((size/2) - 0.5):])
        count += first_count + second_count
    result_array, result_count = merge_and_count(first_half, second_half)
    result_count += count
    return result_array, result_count

def merge_and_count(array1, array2):
    output_array = []
    pointer1 = 0
    pointer2 = 0
    length1 = len(array1)
    length2 = len(array2)
    count = 0
    while ((length1 > 0) and (length2 > 0)):
        element1 = array1[pointer1]
        element2 = array2[pointer2]
        if element2 <= element1:
            output_array.append(element2)
            count += (len(array1) - pointer1)
            pointer2 += 1
            length2 -= 1
        else:
            output_array.append(element1)
            pointer1 += 1
            length1 -= 1
    if length1 == 0:
        for i in range(pointer2, len(array2)):
            output_array.append(array2[i])
        return output_array, count
    elif length2 == 0:
        for i in range(pointer1, len(array1)):
            output_array.append(array1[i])
        return output_array, count

size = int(input())
array = list(map(int, input().split(" ")))
result_array, result_count = merge_sort(size, array)
print(result_count)