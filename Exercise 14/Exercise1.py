a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def getList(a):
    print(commonElements(a))
    

def commonElements(a):
    c = set()
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for a1 in a:
        if not (a1 in b):
            c.add(a1)
    return c

getList(a)