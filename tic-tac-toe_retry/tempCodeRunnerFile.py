if userinput == 1:
                if board[0] != "x" or board[0] != "o":
                    board[0] = "x"
                    print(board[0:3])
                    print(board[3:6])
                    print(board[6:10])
                    comturn()
                else:
                    print("Sorry, that space was already taken. Try Again!")
                    userturn()
        else:
            print("Something went wrong, please try aga