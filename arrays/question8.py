def remove_duplicates(arr):
    duplicates = {}

    # iterate through arr, removing duplicates in place
    for i in range(len(arr)):
        if i >= len(arr):
            break
        if arr[i] in duplicates:
            del arr[i]
        else:
            duplicates[arr[i]] = 1

# test remove_duplicates function
numbers = [1,66,32,34,2,33,11,32,87,3,4,16,55,23,66]
arr = [i for i in numbers]
remove_duplicates(arr)
print("Numbers: ", numbers)
print("Duplicates Removed: ", arr)
