def iterative_quicksort(arr, begin=0, end=None, counter=0):
    '''iterative_quicksort is a recursive quicksorting algorithm'''

    # initialize values on first iteration
    if end is None:
        end = len(arr)-1

    # sort until begin is greater than or equal to end
    if begin < end:

        # starting index, counts size of group lesser than pivot
        i = begin

        # iterate from begin to end, swaping elements to correct side of pivot(end)
        for j in range(begin, end):
            counter += 1
            if arr[j] <= arr[end]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        # smaller elements are in range [begin..i] (inclusive)
        # larger elements are in range [i+1..end-1]

        # swap first element in group greater than pivot with the pivot
        arr[i], arr[end] = arr[end], arr[i]
        # now pivot is at index i+1
        # smaller elements are in range [begin..i]
        # larger elements are in range [i+2..end]

        # sort items before partition and after partition
        counter += iterative_quicksort(arr, begin, i-1)
        counter += iterative_quicksort(arr, i+1, end)

    # return total number of iterations it took to sort
    return counter


## TEST ##
arr = [7, 10, 4, 3, 20, 15, 14, 13, 12, 10, 9,
       8, 7, 6, 4, 3, 1, 4, 6, 82, 81, 1, 19, 24]
arr = arr + arr
print("Numbers:", arr)
counter = iterative_quicksort(arr)
print("Iterations:", counter)
print("Sorted:", arr)
