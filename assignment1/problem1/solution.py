# Name: Jonathan Mychack
# Date Last Accessed: 8/30/20
# Course : CMPSC 465
# Assignment 1, Problem 1


def merge_two_sorted_arrays(array1, array2):
    output_array = [int(array1[0]) + int(array2[0])]
    size_count1 = 1
    size_count2 = 1
    for i in range(1, len(array1) + len(array2)):
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


array1 = list(map(int, input().split(" ")))
array2 = list(map(int, input().split(" ")))
result = merge_two_sorted_arrays(array1, array2)
for i in range(len(result)):
    if i == len(result) - 1:
        print(int(result[i]))
    else:
        print(int(result[i]), end = " ")
