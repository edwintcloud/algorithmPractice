def wiggle_sort(arr):
    '''wiggle_sort sorts an arr such that every other item is greater than or less than it's neighbors'''
    for i in range(len(arr)-1):
        if (i % 2 == 0 and arr[i] > arr[i+1]) or (i % 2 == 1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]

## TEST ##
arr = [3,5,2,1,6,4]
print("Array: ", arr)
wiggle_sort(arr)
print("Wiggle wiggle wiggle yeah: ", arr)