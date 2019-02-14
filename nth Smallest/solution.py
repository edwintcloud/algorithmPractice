def nth_smallest(arr, n):
    '''nth_smallest returns the nth smallest integer in an unsorted integer list'''

    # if n if more than length of arr or less than 0, raise exception
    if n < 0 or n >= len(arr):
        raise Exception(
            'n is less than 0 or greater than length of input list')

    # if len(arr) is 2 then we can just do a single swap
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

    pivot = len(arr)-2
    while pivot > 0:
        for i in range(pivot):
            if arr[pivot] > arr[pivot+1]:
                arr[pivot], arr[pivot+1] = arr[pivot+1], arr[pivot]
            if arr[pivot] < arr[i]:
                arr[pivot], arr[i] = arr[i], arr[pivot]
            if arr[pivot] > arr[pivot+1]:
                arr[pivot], arr[pivot+1] = arr[pivot+1], arr[pivot]
        pivot -= 2

    return arr[n-1]


## TEST ##
arr = [7, 10, 4, 3, 20, 15]
n = 3
print(arr)
result = nth_smallest(arr, n)
print("The", str(n)+"th", "smallest element is:", result)
print(arr)
