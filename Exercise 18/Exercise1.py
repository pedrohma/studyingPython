import random

def generateRandomNumber():
    b = []
    a = random.sample(range(9999), 1)
    while(a[0] < 1000):
        a = random.sample(range(9999), 1)
    a = str(a).replace('[','').replace(']','')
    for number in a:
        b.append(int(number))
    return b

def checkCowNBull(number, guessedNumber):
    win = False
    cow = 0
    bull = 0
    i = 0
    for m in guessedNumber:
        if(number[i] == m):
            cow = cow + 1
        elif(m in number):
            bull = bull + 1
        i = i + 1
        
    print("Cow:" + str(cow) + " Bull: " + str(bull))
    if(cow == 4):
        print("You win!")
        win = True
    return win

win = False               
print("Welcome to Cows And Bulls!")
number = generateRandomNumber()
print(number)
while(win != True):
    guessedNumber = input("Type 4 numbers:")
    arrayGuessednumber = []
    for n in guessedNumber:
        arrayGuessednumber.append(int(n))
    win = checkCowNBull(number, arrayGuessednumber)


