# binary search
# using the fact that our array is already sorted, we can find an element in an
# array by recursively dividing the array in half until the middle element is
# equal to the element we are searching for
# runtime: O(log n)
def binary_search(arr, elem, begin=0, end=None):
    if end is None:
        end = len(arr)
    if end >= begin:
        middle = int(begin + (end-begin)/2)
        if arr[middle] == elem:
            return middle
        elif arr[middle] > elem:
            return binary_search(arr, elem, begin, middle-1)
        else:
            return binary_search(arr, elem, middle+1, end)
    else:
        return None


# test binary search
arr = []
for i in range(1, 36):
    arr.append(i)
result = binary_search(arr, 23)
print("Numbers: ", arr)
if result:
    print("Element 23 found at index: ", result)
else:
    print("Element 23 not found in array!")