def missing_ranges(n, lower, upper):

    # initialize a list to hold our results
    result = []

    # determine if there is a gap from lower to n
    if lower != n[0]:
        result = gap_finder(lower, n[0], result)

    # loop through n, comparing current element to next element
    # if there is a gap, add the gap to result
    for i in range(len(n)-1):
        result = gap_finder(n[i], n[i+1], result)
    
    # determine if there is a gap from n to upper
    if upper != n[-1]:
        result = gap_finder(n[-1], upper+1, result)

    # result list of missing ranges
    return result

def gap_finder(low, high, memo):

        # determine gap
        gap = high - low

        # if gap is greater than 1 number, append range
        # if gap is only one number, append missing number
        # otherwise there is no gap, continue
        if gap > 2:
            memo.append(str(low+1) + "->" + str(high-1))
        elif gap == 2:
            memo.append(str(low+1))
        
        # return memo
        return memo

## TEST ##
tests = [
    ([0, 1, 3, 50, 75], 0, 99),
    ([16, 16, 18, 50, 75], 0, 199),
    ([1,2,3,29,35,66,101], 0, 101)

]
for test in tests:
    print("Numbers:", test)
    print("Missing:", missing_ranges(test[0], test[1], test[2]))