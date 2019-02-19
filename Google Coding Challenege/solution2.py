# Similar to Meeting Rooms II but with separate start time and end time arrays

# Time Complexity: O(n log n)
# Space Complexity: O(n)
def solution(S, E):

    # ensure S and E are equal length
    if len(S) != len(E):
        return Exception("each start time must have an end time!")

    # create a dictionary to map times to time coefficients
    times = {}

    # populate times
    for i in range(len(S)):
        if S[i] in times:
            times[S[i]] += 1
        else:
            times[S[i]] = 1
        if E[i] in times:
            times[E[i]] -= 1
        else:
            times[E[i]] = -1

    # convert times to sorted list of tuples
    times = sorted(times.items(), key=lambda k: k[0])

    # we need a running count and max count
    count = 0
    max_count = 0

    # loop through times, adding value to count
    # max count will hold the highest value running count
    # gets to, which is our answer
    for i in range(len(S)):
        count += times[i][1]
        max_count = max(max_count, count)
    
    # return max_count - the number of chairs needed
    return max_count
