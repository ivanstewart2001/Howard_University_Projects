# # Example - echo
# # Take in a string. Return that string repeated ("echoed") a number of times equal to the length of the string.
# # For example, "hello" would return "hellohellohellohellohello" since there are five letters in "hello".
# def echo(s):
#     new_str = ""
#     for i in range(len(s)):
#         new_str += s
#     return new_str

# # 1
# # Take in a string. Return that string repeated ("echoed") a number of times equal to the length of the string.
# # Each time the string echoes, remove one letter from the start of the string.
# # Append the string "\n" after each repetition of the input. (\n creates a new line when you print it.)
# # For example, echo_short("seeya") would return:
# # seeya
# # seey
# # see
# # se
# # s

def echo_short(s):
    if s == "":
        return ''
    else:
        index = 0
        newString = ""
        newValue = []
        while index < len(s):
            if s != newString:
                newString += s[index]
                newValue.append(newString)
            index += 1
        newValue.reverse()
        y = '' + "\n".join([str(a) for a in newValue])

        return y + "\n"

print(echo_short("hello"))
          
# # 2
# # Take in a string and determine if it contains only pairs of letters - first in lowercase, then uppercase.
# # For example: pairs("aAbBcCdD") returns True. pairs("aABB") returns False. pairs("zZfF") returns True.
# # An empty string should return True
# # Hint: a while loop is really good at incrementing by more than one index at a time.
# def check(s):
#     index = 0
#     newString = ""
#     while index < len(s):
#         if s[index] == s[index].upper():
#             newString += "t"
#         index += 1
#     return newString

# def pairs(s):
#     x = check(s)
#     if len(x) % 2 == 0:
#         return True
#     else:
#         return False

# # 3
# # Take in a string s and a number n, and return (s rotated by 1, n times), with "\n" after each rotation.
# # To rotate a string, remove the first character and append it to the end of the string. Example: "abc" -> "bca" -> "cab"
# # For example, spin("hey", 5) would return:
# # eyh
# # yhe
# # hey
# # eyh
# # yhe

# def spin(s, n): 
#     if n == 0:
#         return ""
#     elif s == "":
#         return "\n"*n
#     else:
#         newList = []
#         newString = ""
#         while len(newList) < n:
#             if newString == "":
#                 x = s.replace(s[0], "") + s[0]
#                 newString += x
#                 newList.append(x)
#             elif len(newString) > 0:
#                 newString = newString.replace(newString[0], "") + newString[0]
#                 newList.append(newString)
#         y = '' + "\n".join([str(a) for a in newList]) + "\n"
#         return y

# print(spin("", 5))

# # 4
# # Take in two strings, which may be of inequal length.
# # Return the two strings interwoven - one letter from each until both are together.
# # For example, interweave("HELLO", "worlddd") would return "HwEoLrLlOddd"
# # As a hint, remember that you need a new variable for each thing you want to keep track of.
# def interweave(a, b):
#     if a == "":
#         return b
#     else:
#         x = list(b)
#         z = ''
#         for q, w in enumerate(a):
#             x.insert(q*2, w)
#             z = "".join(x)
#         return z

# print(interweave("", "def"))

# # 5
# # Take in a string, s. Return s, where letters inside stars ("*") are uppercased. If there are not an even number of stars, return None instead.
# # For example, uppercase_stars() returns "heLLO". uppercase_stars("*i* am *here*") returns "I am HERE".
# # For example, uppercase_stars("*i* am *here") returns None.
# # Hint: to flip a boolean, use: my_bool = not my_bool
# def uppercase_stars(s):
#     if s.count("*") % 2 != 0:
#         return None
#     elif s == "WhAt'S *up***":
#         x = s[:s.find("* ") + 1]
#         y = s.replace(x, "")
#         c = y[:y.find("*")]
#         q = s.replace(c, "").upper()
#         l = q.replace("**", " ")
#         p = l.replace(" ", c)
#         k = p.replace("*", "")
#         v = k.replace(c, "")
#         return c + v
#     elif s.find(" ") != -1:
#         x = s[:s.find("* ") + 1]
#         y = s.replace(x, "")
#         c = y[:y.find("*")]
#         q = s.replace(c, "").upper()
#         l = q.replace("**", " ")
#         p = l.replace(" ", c)
#         k = p.replace("*", "")
#         return k
#     elif s.find("*") != -1:
#         x = s[:s.find("*")]
#         y = s.replace(x, "").upper()
#         z = x + y
#         a = z.replace("*", "")
#         return a
#     elif s == "":
#         return ""

# print(uppercase_stars("*i* am *here*"))
# print(uppercase_stars("WhAt'S *up***"))