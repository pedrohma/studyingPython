endGame = False
while(endGame != True):
    print("Use the following structure: R -> Rock, P -> Paper, S -> Scissors")
    play = input("Type your play:")
    print("Use the following structure: R -> Rock, P -> Paper, S -> Scissors")
    play2 = input("Type your play:")

    if(play == "R"):
        if(play2 == "R"):
            print("Tied..")
        elif(play2 == "P"):
            print("Player 2 won")
            endGame = True
        else:
            print("Player 1 won")
            endGame = True 
    elif(play == "P"):
        if(play2 == "R"):
            print("Player 1 won")
            endGame = True
        elif(play2 == "P"):
            print("Tied..")
        else:
            print("Player 2 won")
            endGame = True 
    else:
        if(play2 == "R"):
            print("Player 2 won")
            endGame = True
        elif(play2 == "P"):
            print("Player 1 won")
            endGame = True 
        else:
            print("Tied..") 

    if(endGame):
        res = input("Do you wanna play again? (Type 'Y'/'N')")
        if(res == "Y"):
            endGame = False
        else:
            print("Finishing game...")
