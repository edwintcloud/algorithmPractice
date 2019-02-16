def palindrome_perm(s):

    # create a set to hold characters of string
    chars = set()

    # loop over the characters in the string
    # if the character is in set, remove it
    # otherwise add the character to the set
    for i in range(len(s)):
        if s[i] in chars:
            chars.remove(s[i])
        else:
            chars.add(s[i])

    # once loop finishes, the set should contain
    # only characters that were seen once
    # we know that s contains a palindrome if
    # there are 1 or less unique characters
    return len(chars) <= 1

## TEST ##
tests=[
  "code",
   "aab",
"carerac"
]
for test in tests:
    print(test, palindrome_perm(test))