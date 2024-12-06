            if userinput == 1 or userinput == 2 or userinput == 3 or userinput ==4  or userinput == 5 or userinput == 6 or userinput == 7 or userinput == 8 or userinput == 9:
                if board[userinput-1] != "x" or board[userinput-1] != "o":
                    board[userinput-1] = "x"
                    print(board[0:3])
                    print(board[3:6])
                    print(board[6:10])
                    userturn1 = userturn1+1
                    comturn()