# def pre_spin(s): 
#     newList = []
#     first = s[0]
#     second = s[1:]
#     x = second + first
#     newList.append(x)
#     return newList

def spin(s, n): 
    newList = []
    newString = ""
    while len(newList) < n:
        if newString == "":
            x = s.replace(s[0], "") + s[0]
            newString += x
            newList.append(x)
        elif len(newString) > 0:
            newString = newString.replace(newString[0], "") + newString[0]
            newList.append(newString)
    y = '' + "\n".join([str(a) for a in newList])
    return y

print(spin("hey", 5))

