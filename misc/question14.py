def find_triplets(arr):
    triplets = []

    # outer loop will go from first element to next to last element
    for i in range(len(arr)-1):

        # we need a set to hold elements previously visited
        s = set()

        # inner loop will go from second element to last element
        for j in range(i+1, len(arr)):

            # to get 0 we need two numbers that add up to be the positive
            # inverse of a negative number
            if -(arr[i] + arr[j]) in s:
                # we are appending a list of [the previously visited number, current, next]
                triplets.append([-(arr[i] + arr[j]), arr[i], arr[j]])
            else:
                s.add(arr[j])

    # return triplets
    return triplets


arr = [0, -1, 2, -3, 1, 4, 9, 12, 11, -11, 1]
result = find_triplets(arr)
print(arr)
for i in result:
    print(i, "= 0")
