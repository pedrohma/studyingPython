a = [5, 10, 15, 20, 25]

def newList(a):
    b = a[0]
    c = a[(len(a) - 1)]
    d = []
    d.append(b)
    d.append(c)
    return d

print(newList(a))