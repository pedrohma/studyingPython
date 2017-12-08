from random import randint

a = []
b = []

for x in range(0,12):
    a.append(randint(0, 100))

for y in range(0,20):
    b.append(randint(0,100))

print(a)
print(b)

for a1 in a:
    for b1 in b:
        if(a1 == b1):
            print(str(a1) + " is on both lists.")