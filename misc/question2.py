# iterative quicksort (recursive quicksort)
def iterative_quicksort(arr, begin=0, end=None):
    if end is None:
        end = len(arr)-1
    
    # sort until begin is greater than or equal to end
    if begin < end:

        i = begin-1

        # iterate from begin to end, swaping elements to correct side of pivot(end) index (partition)
        for j in range(begin, end):
            if arr[j] <= arr[end]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            
        # swap last two elements
        arr[i+1], arr[end] = arr[end], arr[i+1]

        # sort items before partition and after partition
        iterative_quicksort(arr, begin, i)
        iterative_quicksort(arr, i+2, end)

# test function
arr = [2,4,5,1,3,29,9,2,12,87]
print("Number: ", arr)
iterative_quicksort(arr)
print("Sorted: ", arr)