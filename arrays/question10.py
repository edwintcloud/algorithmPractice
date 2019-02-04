def remove_duplicates(arr):
    arr[:] = list({i:0 for i in arr})

# test remove_duplicates
numbers = [1,66,32,34,2,33,11,32,87,3,4,16,55,23,66]
arr = [i for i in numbers]
remove_duplicates(arr)
print("Numbers: ", numbers)
print("Duplicates Removed: ", arr)