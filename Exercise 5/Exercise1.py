a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for a1 in a:
    for b1 in b:
        if(a1 == b1):
            print(str(a1) + " is on both lists.")