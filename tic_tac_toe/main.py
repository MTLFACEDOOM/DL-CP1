#Devin longtree [Tic Tac Toe Game]
import random
board1 = [1,2,3]
board2 = [4,5,6]
board3 = [7,8,9]
cominput = random.randint(1,9)


def userwin():
#horizontal
    if board1[0] == "x" and board1[1] == "x" and board1[2] == "x":
        print("You Win!")
    if board2[0] == "x" and board2[1] == "x" and board2[2] == "x":
        print("You Win!")
    if board3[0] == "x" and board3[1] == "x" and board3[2] == "x":
        print("You Win!")
#Vertical
    if board1[0] == "x" and board2[0] == "x" and board3[0] == "x":
        print("You Win!")
    if board1[1] == "x" and board2[1] == "x" and board3[1] == "x":
        print("You Win!")
    if board1[2] == "x" and board2[2] == "x" and board3[2] == "x":
        print("You Win!")
#Diagonal
    if board1[0] == "x" and board2[1] == "x" and board3[2] == "x":
        print("You Win!")
    if board1[2] == "x" and board2[1] == "x" and board3[0] == "x":
        print("You Win!")

def comwin():
    #horizontal
    if board1[0] == "o" and board1[1] == "o" and board1[2] == "o":
        print("Computer Wins!")
    if board2[0] == "o" and board2[1] == "o" and board2[2] == "o":
        print("Computer Wins!")
    if board3[0] == "x" and board3[1] == "o" and board3[2] == "o":
        print("Computer Wins!")
#Vertical
    if board1[0] == "o" and board2[0] == "o" and board3[0] == "o":
        print("Computer Wins!")
    if board1[1] == "o" and board2[1] == "o" and board3[1] == "o":
        print("Computer Wins!")
    if board1[2] == "o" and board2[2] == "o" and board3[2] == "o":
        print("Computer Wins!")
#Diagonal
    if board1[0] == "o" and board2[1] == "o" and board3[2] == "o":
        print("You Win!")
    if board1[2] == "o" and board2[1] == "o" and board3[0] == "o":
        print("Computer Wins!")
#a
def complay():
    cominput = random.randint(1,9)
    print(cominput)
    if cominput == 1:
        if board1[0] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board1[0] != "x":
            board1[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if cominput == 2:
        if board1[1] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if cominput == 3:
        if board1[2] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()

    if cominput == 4:
        if board2[0] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board2[0] != "x":
            board2[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if cominput == 5:
        if board2[1] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board2[1] != "x":
            board2[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if cominput == 6:
        if board2[2] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board2[2] != "x":
            board2[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()

    if cominput == 7:
        if board3[0] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board3[0] != "x":
            board3[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if cominput == 8:
        if board3[1] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board3[1] != "x":
            board3[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if cominput == 9:
        if board3[2] == "x":
            print("Com Input error. Retrying.")
            complay()
        elif board3[2] != "x":
            board3[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()

def userplay():
    print(board1)
    print(board2)
    print(board3)
    userinput = int(input("Please enter a number from 1-9: "))
#board1
    if userinput == 1:
        if board1[0] == "x":
            print("Sorry! This space is already taken!")
        elif board1[0] != "x":
            board1[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()

    if userinput == 2:
        if board1[1] == "x":
            print("Sorry! This space is already taken!")    
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()

    if userinput == 3:
        if board1[2] == "x":
            print("Sorry! This space is already taken!")
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
#board2
    if userinput == 4:
        if board2[0] == "x":
            print("Sorry! This space is already taken!")
        elif board2[0] != "x":
            board2[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if userinput == 5:
        if board2[1] == "x":
            print("Sorry! This space is already taken!")
        elif board2[1] != "x":
            board2[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if userinput == 6:
        if board2[2] == "x":
            print("Sorry! This space is already taken!")
        elif board2[2] != "x":
            board2[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
#board3
    if userinput == 7:
        if board3[0] == "x":
            print("Sorry! This space is already taken!")
        elif board3[0] != "x":
            board3[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if userinput == 8:
        if board3[1] == "x":
            print("Sorry! This space is already taken!")    
        elif board3[1] != "x":
            board3[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()
    if userinput == 9:
        if board3[2] == "x":
            print("Sorry! This space is already taken!")
        elif board3[2] != "x":
            board3[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            win()

def playloop():
    print("Computer Turn")
    complay()
    print("User Turn")
    userplay()
    choice = input("Do you want to play again? yes/no: ")
    if choice == "yes":
        playloop()
    else:
        print("Ok")
playloop()