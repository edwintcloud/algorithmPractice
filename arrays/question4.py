def sum_pairs(numbers, sum):
    result = []

    # sort the array in reverse order
    arr = sorted(numbers, reverse=True)

    # remove elements larger than sum
    arr[:] = [i for i in arr if i < sum] 

    # go through the sorted array, checking to see if sum - larger number == smaller number
    # if pair is found, append to result and break from the inner loop
    for i in range(len(arr)):
        for j in range(len(arr)-1, 1, -1):
            if sum - arr[i] == arr[j]:
                result.append([arr[j], arr[i]])
                break
    
    # return None if no pairs were found, else return result
    return None if len(result) == 0 else result

# test our sum_pairs function below
numbers = [2,10,6,8,4,22,11,9,13]
sum = 21
results = sum_pairs(numbers, sum)
print("Numbers: ", numbers)
print("Sum: ", sum)
print("Results: ", results)