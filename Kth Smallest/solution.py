def kth_smallest(arr, n):
    '''kth_smallest returns the kth smallest integer in an unsorted integer list
       Runtime: O(n^2)'''

    # if k if more than length of arr or less than 0, raise exception
    if k < 0 or k >= len(arr):
        raise Exception(
            'k is less than 0 or greater than length of input list')

    # a simple counter to count number of iterations
    counter = 0

    # iterate through array, swaping all elements to correct position
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            counter += 1
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

        # break when we get to kth smallest
        if i == k-1:
            break

    print("Iterations:", counter)

    return arr[k-1]


## TEST ##
arr = [7, 10, 4, 3, 20, 15, 14, 13, 12, 10, 9,
       8, 7, 6, 4, 3, 1, 4, 6, 82, 81, 1, 19, 24]
arr = arr + arr
k = 3
print(arr)
result = kth_smallest(arr, k)
print("The", str(k)+"th", "smallest element is:", result)
print(arr)
