from random import randint

number = randint(0,9)

print("Let's play guessing game!")

playAgain = True

while(playAgain):
    userNumber = int(input("Enter a number from 0 to 9"))

    if(number == userNumber):
        print("You won!")
        playAgain == False
    elif (userNumber > number):
        print("Your number was grater than the number...")
    elif(userNumber < number):
        print("Your number was too low than the number...")
    else:
        print()

    resp = input("Do you wanna play again? (Y/exit)")
    if(resp == "exit"):
        playAgain == False
