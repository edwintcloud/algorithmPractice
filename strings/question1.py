def print_duplicates(string):
    counts = {}
    for c in string:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return [k for k,v in counts.items() if v > 1 and k is not " "]

# test duplicates function
string = "Hello I am a sentmensce"
result = print_duplicates(string)
print("String: ", string)
print("Duplicates: ", result)