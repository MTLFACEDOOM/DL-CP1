#Devin Longtree [Tic Tac Toe]
import random
board = ["-","-","-",
         "-","-","-", 
         "-","-","-"]
print(board[0:3])
print(board[3:6])
print(board[6:10])

def userturn():
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
                    comturn()
                if board[userinput-1] == "x" or board[userinput-1] == "o":
                    print("Sorry, that space was already taken. Try Again!")
                    userturn()
            else:
                print("Please put in a number one through nine. Try again.")
                userturn()

def comturn():
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
                    comturn1 = comturn1+1
                    userturn()
                if board[comchoice-1] == "x" or board[comchoice-1] == "o":
                    comturn()
                if board[0] == "x" or board[0] == "o" and 
                    
            userturn()
    userturn()


userturn()

