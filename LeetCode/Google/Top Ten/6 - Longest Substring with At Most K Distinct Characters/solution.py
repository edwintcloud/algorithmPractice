def longest_substring(s, k):
    '''longest_substring finds the longest sequence(s) of characters that 
       satisfies the condition of k characters must be unique'''

    # first check that we have enough unique characters to satisfy k
    if len(set(s)) < k:
        raise Exception("not enough unique characters")

    # create an array to hold our character counts
    # we will use this array to shift a window of
    # characters to search
    counts = [0] * 26

    # initialize begin and end index for result
    begin, end = 0, 0

    # create a set to hold distint characters in the window
    window = set()

    # initialize the left index of our window
    left = 0

    # start the search window process
    for right in range(len(s)):

        # start by adding the character to the window
        window.add(s[right])

        # increment the count at the character position in our counts list
        counts[ord(s[right])-97] += 1

        # remove items from the window until we reach k
        while len(window) > k:

            # decrement the count for the character at the left index
            counts[ord(s[left])-97] -= 1

            # if the count for the character at the left index is 0
            # remove character at left index from the window
            if counts[ord(s[left])-97] == 0:
                window.remove(s[left])

            # increment left to shift our window to the right
            left += 1

        # if our window grows smaller than k, resize the window
        if end - begin < right - left:
            end = right
            begin = left

    # return the character sequence that satisfies k
    return s[begin:end-begin+1]


## TEST ##
tests = [
    ("eceba", 2),
    ("aabbcc", 1),
    ("dopee", 2)
]
for test in tests:
    print("string =", test[0], "k =", test[1])
    t = longest_substring(test[0], test[1])
    print("T:", t, "L:", len(t))
