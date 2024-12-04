#Devin longtree [Tic Tac Toe Game]
import random
board1 = [1,2,3]
board2 = [4,5,6]
board3 = [7,8,9]
print(board1)
cominput = random.randint(1,3)
print(cominput)

def complay():
    if cominput == 1:
        if board1[0] == "x":
            print("Sorry! This space is already taken!")
        elif board1[0] != "x":
            board1[0] = "x"
            print(board1)

    if cominput == 2:
        if board1[1] == "x":
            print("Sorry! This space is already taken!")    
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)

    if cominput == 3:
        if board1[2] == "x":
            print("Sorry! This space is already taken!")
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)

def userplay():
    print(board1)
    userinput = int(input("Please enter a number from 1-9: "))
#board1
    if userinput == 1:
        if board1[0] == "x":
            print("Sorry! This space is already taken!")
        elif board1[0] != "x":
            board1[0] = "x"
            print(board1)

    if userinput == 2:
        if board1[1] == "x":
            print("Sorry! This space is already taken!")    
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)

    if userinput == 3:
        if board1[2] == "x":
            print("Sorry! This space is already taken!")
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)
#board2
    if userinput == 4:
        if board1[0] == "x":
            print("Sorry! This space is already taken!")
        elif board1[0] != "x":
            board1[0] = "x"
            print(board1)

    if userinput == 5:
        if board1[1] == "x":
            print("Sorry! This space is already taken!")    
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)

    if userinput == 3:
        if board1[2] == "x":
            print("Sorry! This space is already taken!")
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)
#board3
    if userinput == 1:
        if board1[0] == "x":
            print("Sorry! This space is already taken!")
        elif board1[0] != "x":
            board1[0] = "x"
            print(board1)

    if userinput == 2:
        if board1[1] == "x":
            print("Sorry! This space is already taken!")    
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)

    if userinput == 3:
        if board1[2] == "x":
            print("Sorry! This space is already taken!")
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)

    choice = input("Do you want to play again? yes/no: ")
    if choice == "yes":
        userplay()
    else:
        print("Ok")

userplay()