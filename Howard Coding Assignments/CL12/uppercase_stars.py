def uppercase_stars(s):
    if s.count("*") % 2 != 0:
        return None
    elif s.find(" ") != -1:
        x = s[:s.find("* ") + 1]
        y = s.replace(x, "")
        c = y[:y.find("*")]
        q = s.replace(c, "").upper()
        l = q.replace("**", " ")
        p = l.replace(" ", c)
        k = p.replace("*", "")
        return k
    elif s.find("*") != -1:
        x = s[:s.find("*")]
        y = s.replace(x, "").upper()
        z = x + y
        a = z.replace("*", "")
        return a

print(uppercase_stars("he*llo*")) #heLLO
print(uppercase_stars("*i* am *here*")) # I am HERE
print(uppercase_stars("*i* am *here")) # none


