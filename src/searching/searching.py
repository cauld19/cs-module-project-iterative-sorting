def linear_search(arr, target):
    count = -1
    for i in range(len(arr)):
        count += 1
        if arr[i] is target:
            return count 


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    
    for _ in range(len(arr)):
        middle = (first + last) // 2
        if target is arr[middle]:
            return arr.index(arr[middle])
        elif target < arr[middle]:
            last = middle - 1
        else:
            first = middle + 1


    return -1  # not found
