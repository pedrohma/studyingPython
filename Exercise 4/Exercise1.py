num = int(input("Choose a number between 1 and 100:"))

x = range(1, 100)

for i in x:
    y = i % num
    if(y == 0):
        print(i)