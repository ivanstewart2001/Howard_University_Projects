def echo(s):
    index = 0
    len_s = len(s)
    newString = ""
    newValue = []
    while index < len(s):
        if s != newString:
            newString += s[index]
            newValue.append(newString)
        index += 1
        len_s -= 1
    x = newValue.reverse()
    y = '' + "\n".join([str(a) for a in newValue])
    return y


print(echo("seeya"))