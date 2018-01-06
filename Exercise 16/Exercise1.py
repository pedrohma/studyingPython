import string
from random import randint

def generatePassword(type):
    lowercaseList = list(string.ascii_lowercase)
    uppercaseList = list(string.ascii_uppercase)
    numberList = range(0,9)
    specialList = list(string.punctuation)
    createPassword(lowercaseList, uppercaseList, numberList, specialList, type)

def createPassword(lowercaseList, uppercaseList, numberList, specialList, type):
    password = ""
    i = 0
    y = 0

    if(type == "STRONG"):
        y = 5
    elif (type == "NORMAL"):
        y = 3
    elif (type == "WEAK"):
        y = 1
    else:
        print("Invalid input.") 
    
    while(i < y):
        j = randint(0, len(lowercaseList))
        k = randint(0, len(uppercaseList))
        l = randint(0, len(numberList))
        m = randint(0, len(specialList))
        password = password + lowercaseList[j] + str(numberList[l]) + specialList[m] + uppercaseList[k]
        i = i + 1
    print(password)

print("Welcome to the Password generator!")
generatePassword(input("What kin of password do you want? STRONG-NORMAL-WEAK?"))