import random
board1 = [1,2,3]
board2 = [4,5,6]
board3 = [7,8,9]
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
    if cominput == 2:
        if board1[1] == "x" or board1[1] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board1[1] != "x" or board1[1] != "o":
            board1[1] = "o"
            print(board1)
            print(board2)
            print(board3)
    if cominput == 3:
        if board1[2] == "x" or board1[2] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board1[2] != "x" or board1[2] != "o":
            board1[2] = "o"
            print(board1)
            print(board2)
            print(board3)

    if cominput == 4:
        if board2[0] == "x" or board2[0] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board2[0] != "x" or board2[0] != "o":
            board2[0] = "o"
            print(board1)
            print(board2)
            print(board3)
    if cominput == 5:
        if board2[1] == "x" or board2[1] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board2[1] != "x" or board2[1] != "o":
            board2[1] = "o"
            print(board1)
            print(board2)
            print(board3)
    if cominput == 6:
        if board2[2] == "x" or board2[2] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board2[2] != "x" or board2[2] != "o":
            board2[2] = "o"
            print(board1)
            print(board2)
            print(board3)

    if cominput == 7:
        if board3[0] == "x" or board3[0] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board3[0] != "x" or board3[0] != "o":
            board3[0] = "o"
            print(board1)
            print(board2)
            print(board3)
    if cominput == 8:
        if board3[1] == "x" or board3[1] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board3[1] != "x" or board3[1] != "o":
            board3[1] = "o"
            print(board1)
            print(board2)
            print(board3)
    if cominput == 9:
        if board3[2] == "x" or board3[2] == "o":
            print("Com Input error. Retrying.")
            complay()
        elif board3[2] != "x" or board3[2] != "o":
            board3[2] = "o"
            print(board1)
            print(board2)
            print(board3)

complay()