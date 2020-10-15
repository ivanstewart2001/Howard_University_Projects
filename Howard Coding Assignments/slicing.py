# def all_except_first(s):
#     """Return the string without the first character.
#     all_except_first("hello") returns "ello" """
#     return s[1:]
    

# print(all_except_first("hello"))

# def last_n_chars(s, n):
#     """Return the final n chars of s.
#     last_n_chars("hello world", 3) returns "rld"
#     You can assume that s is always at least n characters long. """
#     return s[-n:]

# print(last_n_chars("hello world", 3))

# def second_half(s):
#     """Returns the second half of the string (including the middle, if the string is an odd length.)
#     second_half("catsanddogs") returns "nddogs" """
#     if not len(s) % 2  == 0:
#         length = len(s) / 2
#         newLength = int(length)
#         return s[newLength:]
#     else:
#         length = len(s) / 2
#         newLength = int(length)
#         return s[newLength:]


# print(len("helloworld"))
# print(second_half("helloworld"))

# def after_symbol(s, sym):
#     """Return all of the characters after the character given
#     after_symbol("eseidohl@google.com", "@") returns "google.com"
#     after_symbol("eseidohl@google.com", ".") returns "com"
#     You can assume that sym is always one character and always exists in s.
#     Hint: What does .find() do?"""
#     text = s.find(sym)
#     return s[text + 1:]

# print(after_symbol("eseidohl@google.com", "."))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False 

def middle_n(s, n):
    """Returns the middle n characters from a string.
    middle_n("abcdcba", 3) returns "cdc"
    Default toward the end of the list if the selection does not line up exactly.
    middle_n("abcdcba", 4) returns "cdcb"
    This one is more difficult! Use intermediate variables to keep track of values."""
    # striped = s.replace(" ", "")
    # print(len(striped))
    if s.find(" ") != -1:
        # newLength = len(s) + 1
        new_n = n + 1
        half_left = len(s) / new_n
        justified_left = int(half_left)
        text_right = s[justified_left + 2:]
        # text_left = s[:justified_left +1]
        updated = text_right[:n]
        return updated
    elif int(len(s) - n) != is_even(n):
        new_n = n + 1
        half_left = len(s) / new_n
        justified_left = int(half_left)
        text_right = s[justified_left + 1:]
        # text_left = s[:justified_left +1]
        updated = text_right[:n]
        return updated
    else:
        new_n = n + 1
        half_left = len(s) / new_n
        justified_left = int(half_left)
        text_right = s[justified_left + 1:]
        # text_left = s[:justified_left +1]
        updated = text_right[:n+1]
        return updated


print(middle_n("happy birthday", 6))

