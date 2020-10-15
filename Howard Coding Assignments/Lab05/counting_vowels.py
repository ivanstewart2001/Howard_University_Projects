def isVowel(char):
    return char in 'aeiouAEIOU'

def remove_vowels(s):
    index = 0
    vowel_str = ""
    while index < len(s):
        if isVowel(s[index]):
            vowel_str += s[index]
        index += 1
    return vowel_str

def count_vowels(s):
    x = remove_vowels(s)
    y = len(x)
    return y

print(isVowel("A"))
    