#Devin longtree [Tic Tac Toe Game]
import random
board1 = [1,2,3]
board2 = [4,5,6]
board3 = [7,8,9]
cominput = random.randint(1,9)
wincondition = False


def userwin():
    global wincondition
#horizontal
    if board1[0] == "x" and board1[1] == "x" and board1[2] == "x":
        print("You Win!")
        wincondition = True
    if board2[0] == "x" and board2[1] == "x" and board2[2] == "x":
        print("You Win!")
        wincondition = True
    if board3[0] == "x" and board3[1] == "x" and board3[2] == "x":
        print("You Win!")
        wincondition = True
#Vertical
    if board1[0] == "x" and board2[0] == "x" and board3[0] == "x":
        print("You Win!")
        wincondition = True
    if board1[1] == "x" and board2[1] == "x" and board3[1] == "x":
        print("You Win!")
        wincondition = True
    if board1[2] == "x" and board2[2] == "x" and board3[2] == "x":
        print("You Win!")
        wincondition = True
#Diagonal
    if board1[0] == "x" and board2[1] == "x" and board3[2] == "x":
        print("You Win!")
        wincondition = True
    if board1[2] == "x" and board2[1] == "x" and board3[0] == "x":
        print("You Win!")
        wincondition = True
        
    

def comwin():
    global wincondition
#horizontal
    if board1[0] == "o" and board1[1] == "o" and board1[2] == "o":
        print("Computer Wins!")
        wincondition = True
    if board2[0] == "o" and board2[1] == "o" and board2[2] == "o":
        print("Computer Wins!")
        wincondition = True
    if board3[0] == "x" and board3[1] == "o" and board3[2] == "o":
        print("Computer Wins!")
        wincondition = True
#Vertical
    if board1[0] == "o" and board2[0] == "o" and board3[0] == "o":
        print("Computer Wins!")
        wincondition = True
    if board1[1] == "o" and board2[1] == "o" and board3[1] == "o":
        print("Computer Wins!")
        wincondition = True
    if board1[2] == "o" and board2[2] == "o" and board3[2] == "o":
        print("Computer Wins!")
        wincondition = True
#Diagonal
    if board1[0] == "o" and board2[1] == "o" and board3[2] == "o":
        print("YComputer Wins!")
        wincondition = True
    if board1[2] == "o" and board2[1] == "o" and board3[0] == "o":
        print("Computer Wins!")
        wincondition = True

        
#a
def complay():
    cominput = random.randint(1,9)
    print(cominput)
    if cominput == 1:
        if board1[0] == "x" or board1[0] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board1[0] != "x" or board1[0] != "o":
            board1[0] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()
    if cominput == 2:
        if board1[1] == "x" or board1[1] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board1[1] != "x" or board1[1] != "o":
            board1[1] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()
    if cominput == 3:
        if board1[2] == "x" or board1[2] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board1[2] != "x" or board1[2] != "o":
            board1[2] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()

    if cominput == 4:
        if board2[0] == "x" or board2[0] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board2[0] != "x" or board2[0] != "o":
            board2[0] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()
    if cominput == 5:
        if board2[1] == "x" or board2[1] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board2[1] != "x" or board2[1] != "o":
            board2[1] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()
    if cominput == 6:
        if board2[2] == "x" or board2[2] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board2[2] != "x" or board2[2] != "o":
            board2[2] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()

    if cominput == 7:
        if board3[0] == "x" or board3[0] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board3[0] != "x" or board3[0] != "o":
            board3[0] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()
    if cominput == 8:
        if board3[1] == "x" or board3[1] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board3[1] != "x" or board3[1] != "o":
            board3[1] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()
    if cominput == 9:
        if board3[2] == "x" or board3[2] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board3[2] != "x" or board3[2] != "o":
            board3[2] = "o"
            print(board1)
            print(board2)
            print(board3)
            comwin()

def userplay():
    print(board1)
    print(board2)
    print(board3)
    userinput = int(input("Please enter a number from 1-9: "))
#board1
    if userinput == 1:
        if board1[0] == "x" or board1[0] == "o":
            print("Sorry! This space is already taken!")
        elif board1[0] != "x":
            board1[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()

    if userinput == 2:
        if board1[1] == "x" or board1[1] == "o":
            print("Sorry! This space is already taken!")    
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()

    if userinput == 3:
        if board1[2] == "x" or board1[2] == "o":
            print("Sorry! This space is already taken!")
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()
#board2
    if userinput == 4:
        if board2[0] == "x" or board2[0] == "o":
            print("Sorry! This space is already taken!")
        elif board2[0] != "x":
            board2[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()
    if userinput == 5:
        if board2[1] == "x" or board2[1] == "o":
            print("Sorry! This space is already taken!")
        elif board2[1] != "x":
            board2[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()
    if userinput == 6:
        if board2[2] == "x" or board2[2] == "o":
            print("Sorry! This space is already taken!")
        elif board2[2] != "x":
            board2[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()
#board3
    if userinput == 7:
        if board3[0] == "x" or board3[0] == "o":
            print("Sorry! This space is already taken!")
        elif board3[0] != "x":
            board3[0] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()
    if userinput == 8:
        if board3[1] == "x" or board3[1] == "o":
            print("Sorry! This space is already taken!")    
        elif board3[1] != "x":
            board3[1] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()
    if userinput == 9:
        if board3[2] == "x" or board3[2] == "o":
            print("Sorry! This space is already taken!")
        elif board3[2] != "x":
            board3[2] = "x"
            print(board1)
            print(board2)
            print(board3)
            userwin()

def playloop():
    global wincondition
    print("Computer Turn")
    complay()
    print("User Turn")
    userplay()
    if wincondition == True:
        print("Thanks for Playing.")
    if wincondition == False:
            playloop()

playloop()