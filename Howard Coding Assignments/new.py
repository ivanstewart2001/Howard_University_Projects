# def isVowel(string):
#     if string == 'a' or 'e' or 'i' or 'o' or 'u':
#         return True
#     else:
#         return False



def isVowel(char):
    return char in 'aeiouAEIOU'

print(isVowel("hi"))

def remove_vowels(s):
    index = 0
    newString = ""
    while index < len(s):
        if not isVowel(s[index]):
            newString += s[index]
        index += 1
    return newString

print(remove_vowels("hi"))


