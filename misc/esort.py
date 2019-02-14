def e_sort(arr):
    '''e_sort sorts a list in place by pivoting every len(arr)-2 elements
       swaping ith, pivot, and pivot+1 elements to correct order
       Runtime: O(n^2)'''

    # if len(arr) is 2 then we can just do a single swap
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

    # a simple counter to count number of iterations
    counter = 0

    # we start with a pivot of next to last element
    pivot = len(arr)-2

    # outer loop: until pivot is less than or equal to 0
    # each iteration we subtract 2 from pivot
    while pivot > 0:

        # inner loop: from 0 to pivot, we make three comparisons/swaps
        # with pivot to ensure i, pivot, and pivot+1 are in order
        for i in range(pivot):
            if arr[pivot] > arr[pivot+1]:
                arr[pivot], arr[pivot+1] = arr[pivot+1], arr[pivot]
            if arr[pivot] < arr[i]:
                arr[pivot], arr[i] = arr[i], arr[pivot]
            if arr[pivot] > arr[pivot+1]:
                arr[pivot], arr[pivot+1] = arr[pivot+1], arr[pivot]
            counter += 1

        # subtract 2 from pivot
        pivot -= 2

    # return total number of iterations it took to sort
    return counter


## TEST ##
arr = [7, 10, 4, 3, 20, 15, 14, 13, 12, 10, 9,
       8, 7, 6, 4, 3, 1, 4, 6, 82, 81, 1, 19, 24]
arr = arr + arr
print("Numbers:", arr)
counter = e_sort(arr)
print("Iterations:", counter)
print("Sorted:", arr)
