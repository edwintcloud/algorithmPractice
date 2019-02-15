def alien_dict(words):
    '''alien_dict finds the alphabetical order of a language derived using a-z
       from the first few words that would appear in a dictionary of words for the language'''

    # initialize a dictionary to hold the letters than follow each letter in list of words
    graph = {}

    # initialize 0 filled list of alphabet positions
    alphaPositions = [0] * 26

    # initialize a queue we will use to sort the letters once we establish relationships
    queue = []

    # initialize a list we will use to build our result string
    result = []

    # populate graph with each letter maping to an empty set that will hold relations
    for word in words:
        for c in word:
            graph[c] = set()

    # find the letters that follow each letter in our graph
    for i in range(1, len(words)):
        for j in range(min(len(words[i-1]), len(words[i]))):
            if words[i-1][j] != words[i][j]:
                if words[i][j] in graph[words[i-1][j]]:
                    break
                graph[words[i-1][j]].add(words[i][j])

                # mark each alpha position visited
                alphaPositions[ord(words[i][j]) - 97] += 1

    # add c in graph to queue if it has not been visited
    for c in graph:
        if alphaPositions[ord(c) - 97] == 0:
            queue.append(c)

    # go through queue, building result string
    while len(queue) > 0:
        c = queue.pop(0)
        result.append(c)

        # mark neighbors of current queue item as visited,
        # if neighbor was previously visited then add it
        # to the end of the queue
        for neighbor in graph[c]:
            alphaPositions[ord(neighbor)-97] -= 1
            if alphaPositions[ord(neighbor)-97] == 0:
                queue.append(neighbor)

    # join result to string and return
    return "".join(result)


## TEST ##
tests = [
    [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ],
    [
        "z",
        "x"
    ],
    [
        "z",
        "x",
        "z"
    ]
]
for test in tests:
    for i, line in enumerate(test, 1):
        if i == len(test):
            print('"', line, '"]')
        else:
            print('["', line, '",')
    print("The correct order is :", alien_dict(test))
