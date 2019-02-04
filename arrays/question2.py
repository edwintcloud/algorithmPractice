def find_duplicates(arr):
    result = {}

    # first we must sort the array
    arr.sort()

    # next we compare if each next element is same as current
    # if they are the same, add to result
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            if arr[i] in result:
                result[arr[i]] += 1
            else:
                result[arr[i]] = 1

    # return result
    return result

# test our find_duplicates function below
duplicates = [24, 39]
numbers = [0,1]
for i in range(1, 101):
    numbers.append(i)
    if i == duplicates[0] or i == duplicates[1]:
        numbers[i-1] = i
    if i == duplicates[0]:
        numbers[i-2] = i
print(find_duplicates(numbers))
