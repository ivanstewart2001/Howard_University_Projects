def interweave(a, b):
    x = list(b)
    for q, w in enumerate(a):
        x.insert(q*2, w)
        z = "".join(x)
    return z

print(interweave("HELLO", "worlddd"))