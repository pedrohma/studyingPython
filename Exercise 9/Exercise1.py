from random import randint

number = randint(0,9)

print("Let's play guessing game!")

playAgain = True
trying = 0

while(playAgain):
    userNumber = int(input("Enter a number from 0 to 9\n"))

    if(number == userNumber):
        print("You won! You tryed " + str(trying) + " times!")
        resp = input("Do you wanna play again? (Y/exit)\n")
        if(resp == "exit"):
            playAgain == False
        else:
            number = randint(0,9)
            trying = 0
    elif (userNumber > number):
        print("Your number was grater than the number...")
        trying += 1
    elif(userNumber < number):
        print("Your number was too low than the number...")
        trying += 1
    else:
        print()

    
