def check(s):
    index = 0
    newString = ""
    while index < len(s):
        if s[index] == s[index].upper():
            newString += "t"
        index += 1
    return newString



def pairs(s):
    x = check(s)
    if len(x) % 2 == 0:
        return True
    else:
        return False


print(pairs("hHgG"))
