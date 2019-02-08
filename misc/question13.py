def duplicates(arr1, arr2):
    numbers1 = set()
    numbers2 = set()

    for i in range(max(len(arr1), len(arr2)), -1, -1):
        if i < len(arr1):
            if arr1[i] in numbers2:
                print(arr1[i])
                arr1.pop()
            else:
                numbers1.add(arr1.pop())
        if i < len(arr2):
            if arr2[i] in numbers1:
                print(arr2[i])
                arr2.pop()
            else:
                numbers2.add(arr2.pop())
        
## TEST ##
arr1 = [7,1,3,4,5,78,9,78]
arr2 = [3,11,12,33,5,7,4]
print(arr1)
print(arr2)
duplicates(arr1, arr2)
print(arr1)
print(arr2)