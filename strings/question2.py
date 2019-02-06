def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    chars1 = {c.lower():0 for c in string1}
    chars2 = {c.lower():0 for c in string2}
    
    return chars1 == chars2

# test function
string1 = "listen"
string2 = "silent"
string3 = "jackrabbit"
string4 = "tilent"
print("Are", string1, "and", string2, "anagrams?: ", is_anagram(string1, string2))
print("Are", string2, "and", string3, "anagrams?: ", is_anagram(string2, string3))
print("Are", string2, "and", string4, "anagrams?: ", is_anagram(string2, string4))
