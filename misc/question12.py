def is_contiguous(arr, count=0):
    '''is_contiguous searches arr for a contiguous group of 0s
       Input: 2d array,
       Output: bool'''

    # go through our 2d array until we find a 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):

            # once a 0 is found, recursively search neighbors
            # until we hit a 1 or go out of bounds
            if arr[x][y] == 0:
                find_neighbors(arr, x, y)

                # since neighbors were marked as they were visited,
                # count should only be incremented once if the group
                # of 0s is contiguous
                count += 1

    # if count is not greater than 1, return True
    if count == 1:
        return True

    # otherwise, return False
    return False


def find_neighbors(arr, x, y):
    '''find_neighbors is a recursive depth-first search
       to find all neighbors in the 2d array'''

    # make sure we can safely visit current neighbor
    if is_safe(arr, x, y) is False:
        return

    # if we hit a 1 or -1, we are done searching
    if arr[x][y] != 0:
        return

    # set visited neighbors to -1 to mark them
    arr[x][y] = -1

    # indexes to search neighbors
    indexes = [-1, 1, 0, 0]

    # recursively search neighbors in all four directions
    # until we go out of bounds or hit a 1 or -1
    for i in range(len(indexes)):
        find_neighbors(arr, x+indexes[i], y+indexes[-1-i])


def is_safe(arr, x, y):
    '''is_safe checks to make sure we can safely visit a neighbor
       without going out of bounds'''

    if x < 0 or y < 0:
        return False
    if x >= len(arr) or y >= len(arr[x]):
        return False


## TEST ##
arr = [
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 0]
]
print(arr[0])
print(arr[1])
print(arr[2])
print("Is Contiguous: ", is_contiguous(arr), "\n")
arr = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 1, 0]
]
print(arr[0])
print(arr[1])
print(arr[2])
print("Is Contiguous: ", is_contiguous(arr), "\n")
arr = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1]
]
print(arr[0])
print(arr[1])
print(arr[2])
print("Is Contiguous: ", is_contiguous(arr), "\n")
arr = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]
print(arr[0])
print(arr[1])
print(arr[2])
print("Is Contiguous: ", is_contiguous(arr), "\n")
arr = [
    [1, 1],
    [1, 0],
    [1, 0],
    [0, 0],
    [1, 0]
]
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print("Is Contiguous: ", is_contiguous(arr), "\n")
