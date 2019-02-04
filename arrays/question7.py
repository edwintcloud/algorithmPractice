def quick_sort(arr, begin=0, end=None):
    # set end to length - 1 for first iteration
    if end is None:
        end = len(arr) - 1
    
    # when the begin is >= end, we are done
    if begin >= end:
        return
    
    # partiton arr
    pIndex = partition(arr, begin, end)

    # sort elements before partition
    quick_sort(arr, begin, pIndex - 1)

    # sort elements after partition
    quick_sort(arr, pIndex + 1, end)
    
def partition(arr, begin, end):

    # create variable to hold smallest number index
    sIndex = begin

    # iterate through arr, swapping numbers to correct order
    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            sIndex += 1 # increment the index
            arr[sIndex], arr[i] = arr[i], arr[sIndex] # make the swap
        
    # swap smallest with first element in partition
    arr[sIndex], arr[begin] = arr[begin], arr[sIndex]

    # return smallest number index
    return sIndex

# test quick_sort
numbers = [10,7,8,2,22,97,22,45,101,1]
arr = [i for i in numbers]
result = quick_sort(arr)
print("Numbers: ", numbers)
print("Sorted: ", arr)
