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
            if userinput == 1:
                if board[userinput-1] != "x" or board[userinput-1] != "o":
                    board[0] = "x"
                    print(board[0:3])
                    print(board[3:6])
                    print(board[6:10])
                    comturn()
                else:
                    print("Sorry, that space was already taken. Try Again!")
                    userturn()
def comturn():
    comchoice = random.randint(1,9)
    comturn1 = 0
    printed = False
    while comturn1 == 0:
        while printed == False:
            printed = True
            print("The computer chose:",comchoice)
            userturn()
    userturn()


userturn()

