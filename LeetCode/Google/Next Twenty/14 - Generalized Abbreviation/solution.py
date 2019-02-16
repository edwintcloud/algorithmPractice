def generate_abbr(word):

    # create a list to hold our resulting abbreviations
    result = []

    # len(word) bitshift left by 1 is the total amount of
    # abbreviations to generate, this can also be thought of
    # as 1 * 2 ^ len(word)
    for i in range(1 << len(word)):

        # create a list to hold the characters we will
        # later join to a word
        sb = []

        # create k, a counter to count consecutive 1s in x
        # x is a copy of i, we will use x to conditionally
        # build our abbreviation
        k = 0
        x = i

        # build our abbreviation
        for j in range(len(word)):
            if x & 1 == 1:
                k += 1
                if j == len(word) - 1:
                    sb.append(str(k))
            else:
                if k != 0:
                    sb.append(str(k))
                    k = 0
                sb.append(word[j])

            # shift one bit right to continue scanning word
            x = x >> 1

        # join sb to string and append resulting abbreviation
        # to result
        result.append("".join(sb))

    # return  resulting abbreviations
    return result


## TEST ##
print("word")
print(generate_abbr("word"))
print("bike")
print(generate_abbr("bike"))
print("What kind of abbreviations are these anyways?")
print(generate_abbr("poo"))