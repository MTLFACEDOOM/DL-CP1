#Devin Longtree [Tic Tac Toe]
import random
board = ["-","-","-",
         "-","-","-", 
         "-","-","-"]
print(board[0:3])
print(board[3:6])
print(board[6:9])
vertposx1 = [board[i] for i in [0,3,6]]
vertposx2 = [board[i] for i in [1,4,7]]
vertposx3 = [board[i] for i in [2,5,8]]
diagonalx1 = [board[i] for i in [0,4,8]]
diagonalx2 = [board[i] for i in [2,4,6]]

def endscreen():
    print("thank you for playing")
    exit()

def userwin():
    if board[0:3] == ["x","x","x"]:
        print("User wins")
        endscreen()
    if board[3:6] == ["x","x","x"]:
        print("User wins")
        endscreen()
    if board[6:9] == ["x","x","x"]:
        print("User wins")
        endscreen()
    if vertposx1 == ["x","x","x"]:
        print("User wins")
        endscreen()
    if vertposx2 == ["x","x","x"]:
        print("User wins")
        endscreen()
    if vertposx3 == ["x","x","x"]:
        print("User wins")
        endscreen()
    if diagonalx1 == ["x","x","x"]:
        print("User wins")
        endscreen()
    if diagonalx2 == ["x","x","x"]:
        print("User wins")
        endscreen()
def comwin():
    if board[0:3] == ["o","o","o"]:
        print("Com wins")
        endscreen()
    if board[3:6] == ["o","o","o"]:
        print("Com wins")
        endscreen()
    if board[6:9] == ["o","o","o"]:
        print("Com wins")
        endscreen()
    if vertposx1 == ["o","o","o"]:
        print("Com wins")
        endscreen()
    if vertposx2 == ["o","o","o"]:
        print("Com wins")
        endscreen()
    if vertposx3 == ["o","o","o"]:
        print("Com wins")
        endscreen()
    if diagonalx1 == ["o","o","o"]:
        print("Com wins")
        endscreen()
    if diagonalx2 == ["o","o","o"]:
        print("Com wins")
        endscreen()


        print("User wins")
        endscreen()
        

def userturn():
    global vertposx1
    global vertposx2
    global vertposx3
    global diagonalx1
    global diagonalx2
    printed = False
    userturn1 = 0
    userinput = int(input("Input a numer 1-9: "))
    while userturn1 == 0:
                while printed == False:
                    printed = True
                if userinput == 1 or userinput == 2 or userinput == 3 or userinput ==4  or userinput == 5 or userinput == 6 or userinput == 7 or userinput == 8 or userinput == 9:
                    if board[userinput-1] != "x" and board[userinput-1] != "o":
                        board[userinput-1] = "x"
                        print(board[0:3])
                        print(board[3:6])
                        print(board[6:10])
                        userturn1 = userturn1+1
                        vertposx1 = [board[i] for i in [0,3,6]]
                        vertposx2 = [board[i] for i in [1,4,7]]
                        vertposx3 = [board[i] for i in [2,5,8]]
                        diagonalx1 = [board[i] for i in [0,4,7]]
                        diagonalx2 = [board[i] for i in [2,4,6]]
                        userwin()
                        comturn()
                    if board[userinput-1] == "x" or board[userinput-1] == "o":
                        print("Sorry, that space was already taken. Try Again!")
                        userturn()
                else:
                    print("Please put in a number one through nine. Try again!")
                    userturn()


def comturn():
    global vertposx1
    global vertposx2
    global vertposx3
    global diagonalx1
    global diagonalx2
    comchoice = random.randint(1,9)
    comturn1 = 0
    printed = False
    while comturn1 == 0:
            while printed == False:
                printed = True
                if comchoice == 1 or comchoice == 2 or comchoice == 3 or comchoice == 4 or comchoice == 5 or comchoice == 6 or comchoice == 7 or comchoice == 8 or comchoice == 9:
                    if board[comchoice-1] != "x" and board[comchoice-1] != "o":
                        board[comchoice-1] = "o"
                        print("The computer chose:", comchoice)
                        print(board[0:3])
                        print(board[3:6])
                        print(board[6:10])
                        vertposx1 = [board[i] for i in [0,3,6]]
                        vertposx2 = [board[i] for i in [1,4,7]]
                        vertposx3 = [board[i] for i in [2,5,8]]
                        diagonalx1 = [board[i] for i in [0,4,7]]
                        diagonalx2 = [board[i] for i in [2,4,6]]
                        comwin()
                        comturn1 = comturn1+1
                        userturn()
                    if board[comchoice-1] == "x" or board[comchoice-1] == "o":
                        comturn()
                        

userturn()

