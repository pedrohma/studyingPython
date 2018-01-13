import random

lst = [i for i in range(random.randrange(0,1000))]
n = int(input("Enter a number to see if it's in the list range: "))

def isInList(list, number):
    if number in list:
        return True
    else:
        return False

if isInList(lst,n) == True:
	print(str(n) + " is in the list range")
else:
    print(str(n) + " is NOT in the list range")