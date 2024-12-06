import random
board1 = [1,2,3]
board2 = [4,5,6]
board3 = [7,8,9]
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

    if userinput == 2:
        if board1[1] == "x" or board1[1] == "o":
            print("Sorry! This space is already taken!")    
        elif board1[1] != "x":
            board1[1] = "x"
            print(board1)
            print(board2)
            print(board3)

    if userinput == 3:
        if board1[2] == "x" or board1[2] == "o":
            print("Sorry! This space is already taken!")
        elif board1[2] != "x":
            board1[2] = "x"
            print(board1)
            print(board2)
            print(board3)

userplay()