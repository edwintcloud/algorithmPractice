# find_peak is a recursive function that uses divide and conquer methodolology (similar to binary search)
# to find the index of a peak element in O(log n) time complexity
def find_peak(arr, begin=0, end=None, l=None):
    
    # initialize values on first iteration
    if end is None or l is None:
        l = len(arr)
        end = l-1
    
    # find index of middle element
    mid = int(begin + (end - begin) / 2) # truncate result to an int

    
    try:
        # base case: first check if middle is a peak element
        # if it is, return it
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return mid
    
        # if left element is greater than mid, left half must contain a peak;
        # run function again on left half of arr
        if arr[mid-1] > arr[mid]:
            return find_peak(arr, begin, mid-1, l)

        # if right element is greater than mid, right half must contain a peak;
        # run function again on right half of arr
        if arr[mid+1] > arr[mid]:
            return find_peak(arr, mid+1, end, l)
        
    except IndexError:
        
        # couldn't find a peak
        # return either 1st or last element index depending on which is bigger
        # peak will be equal to the corner case of begin or end
        if arr[0] > arr[l-1]:
            return 0
        return l-1




# test function
arr = [8,9,10,11,11,12,13,14,15,18]
print(arr)
result = find_peak(arr)
print("Peak Index:", result)
print("Peak:", arr[result])