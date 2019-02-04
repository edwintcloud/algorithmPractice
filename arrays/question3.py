def find_largest(arr):
    largest = 0

    # iterate through array, if current is greater than largest then replace largest with current
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    
    # return largest
    return largest

def find_smallest(arr):
    try:
        smallest = arr[0]
    except IndexError:
        return None

    # iterate through array, if current is less than smallest then replace smallest with current
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    
    # return smallest
    return smallest

# test find_largest and find_smallest functions below
numbers = [4,5,2,12,87,63,43]
largest = find_largest(numbers)
smallest = find_smallest(numbers)
print("Numbers: ", numbers)
print("Largest Number: ", largest)
print("Smallest Number: ", smallest)