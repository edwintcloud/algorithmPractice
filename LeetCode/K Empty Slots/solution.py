def k_empty_slots(flowers, k):
    '''@param flowers:
                list of positions for each day the flowers will bloom
       @param k:
                integer representing the required distance between two bloomed flowers in which no flowers have bloomed
       @return: day satisfying k'''

    # initialize an zero filled list the length of flowers
    days = [0] * len(flowers)

    # fill days with days[position-1] = day
    # the opposite of flowers[day-1] = position
    for i in range(len(flowers)):
        days[flowers[i]-1] = i+1

    # initialize our window left and right indexes
    # left starts at 0
    # right starts at k + 1 (our first window of two blooms)
    left = 0
    right = k + 1

    # initialize result to the length of flowers + 1
    result = len(flowers) + 1

    # loop: shift our window left until right is greater than the length of flowers
    while right < len(flowers):

        # i is our current index in the days list
        # we start i at left + 1
        i = left + 1

        # increment i while i < right and current day is > left day and current day is > right day
        while i < right and days[i] > max(days[left], days[right]):
            i += 1

        # if our current index reaches right we have found a match for k
        # but it may not be the first day, so each time result is set
        # make sure we are setting it to the min of current result and previous result
        # current result is the max of left day and right day
        if i == right:
            result = min(result, max(days[left], days[right]))

        # shift window right by setting left equal to current index
        # and right equal to current index + k + 1
        left = i
        right = i + k + 1

    # if result ends up equal to the length of flowers + 1,
    # a day was not found satisfying k; return -1.
    # otherwise return result
    return -1 if result == len(flowers) + 1 else result


## TEST ##
tests = [
    ([1, 3, 2], 1),
    ([1, 2, 3], 1),
    ([3, 2, 6, 1, 4, 5], 2),
    ([5, 6, 1, 2, 3, 4], 1)
]
for _, (flowers, k) in enumerate(tests):
    result = k_empty_slots(flowers, k)
    print("flowers:", flowers)
    print("k:", k)
    print("Output:", result)
