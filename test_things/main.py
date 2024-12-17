board = ["o","-","x",
         "-","x","-", 
         "x","-","o"]
print(board[0:3])
print(board[3:6])
print(board[6:9])
vertposx1 = [board[i] for i in [0,3,6]]
vertposx2 = [board[i] for i in [1,4,7]]
vertposx3 = [board[i] for i in [2,5,8]]
diagonalx1 = [board[i] for i in [0,4,8]]
diagonalx2 = [board[i] for i in [2,4,6]]
print(diagonalx1)