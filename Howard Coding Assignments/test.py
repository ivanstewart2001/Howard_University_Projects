def isVowel(char):
    return char in 'aeiouAEIOU'

def remove_vowels(s):
    index = 0
    newString = ""
    while index < len(s):
        if not isVowel(s[index]):
            newString += s[index]
        index += 1
    return newString


print(remove_vowels("qwertyuiop"))

