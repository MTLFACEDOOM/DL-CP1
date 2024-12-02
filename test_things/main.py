import random
cominput = random.randint(1,9)
board1 = [1,2,3]
board2 = [4,5,6]
board3 = [7,8,9]
print(board1)
print(board2)
print(board3)
print(cominput)
if cominput == 1:
    board1[0] = "x"
if cominput == 2:
    board1[1] = "x"
if cominput == 3:
    board1[2] = "x"

if cominput == 4:
    board2[0] = "x"
if cominput == 5:
    board2[1] = "x"
if cominput == 6:
    board2[2] = "x"

if cominput == 7:
    board3[0] = "x"
if cominput == 8:
    board3[1] = "x"
if cominput == 9:
    board3[2] = "x"
print(board1)
print(board2)
print(board3)