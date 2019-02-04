def find_missing(numbers):
    result = []

    # first we must sort the array
    arr = sorted(numbers)

    # next we iterate through, looking to see if the next element exists
    # if the element doesn't exist, we append the missing element to result
    for i in range(len(arr)-1):
        next = arr[i]+1
        if arr[i+1] != next:
            result.append(next)
    
    # return result
    return result if len(result) > 1 else result[0]

# test our find_missing function below
omit = 23
numbers = []
for i in range(1, 100):
    if i != omit:
        numbers.append(i)
result = find_missing(numbers)
print("Numbers: ", numbers)
print("Missing Numbers: ", result)