def meeting_rooms(arr):
    '''meeting_rooms finds the number of meeting rooms 
    needed based on the input arr of lists of start time, end time
    Time Complexity: O(n+n+n log n) => O(n log n)'''

    # create a dictionary
    times = {}

    # populate dicitionary with time coefficients (measuring distance from norm of 0)
    # for each start time, we add 1 to the value associated with time(key)
    # for each end time, we subtract 1 from the value associated with time(key)
    # O(n)
    for i in range(len(arr)):
        if arr[i][0] in times:
            times[arr[i][0]] += 1
        else:
            times[arr[i][0]] = 1
        if arr[i][1] in times:
            times[arr[i][1]] -= 1
        else:
            times[arr[i][1]] = -1

    # convert dictionary to sorted list of tuples: O(n log n)
    times = sorted(times.items(), key=lambda k: k[0])

    # create running count and maximum count variables, initialized to 0
    count, maxcount = 0, 0

    # iterate over list of times, adding coefficient to running count
    # maximum count is set to the larger of running count and current maximum count
    for i in range(len(arr)):
        count += times[i][1]
        maxcount = max(maxcount, count)

    # return the maximum count which will be the number of meeting rooms needed
    return maxcount


## TEST ##
count = meeting_rooms([[0, 30], [5, 10], [15, 20]])
print("Meeting Rooms:", count)
