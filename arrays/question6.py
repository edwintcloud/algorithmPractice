def remove_duplicates(arr):
    return list({i:0 for i in arr})

# test remove_duplicates function
numbers = [1,2,3,4,9,8,7,7,5,22,97,64,22,12]
result = remove_duplicates(numbers)
print("Numbers: ", numbers)
print("Numbers w/o Duplicates: ", result)