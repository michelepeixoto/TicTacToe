def new_board():
    board = []
    for i in range(9):
        board.append(i)
        pass
    return board

def show_board(board):
    drawing = ""
    for a in range(len(board)):
        drawing += "["+str(board[a])+"]"
        if (a==2 or a==5 or a==8):
            drawing = drawing + "\n"
        pass
    print(drawing)
    pass

def next_turn(playerNum, board):
    playerIn = int(input("Player "+str(playerNum)+"\n"))
    if (playerNum==1):
        board[playerIn] = "X"
        pass
    elif (playerNum==2):
        board[playerIn] = "O"
        pass    
    show_board(board)
    if (win_check("X", board)==True):
        print("Player One Wins")
        new_game()
        pass
    elif (win_check("O", board)==True):
        print("Player One Wins")
        new_game()
        pass
    elif (playerNum==1):
        next_turn(2, board)
        pass
    elif (playerNum==2):
        next_turn(1, board)
        pass
    pass

def win_check(player, board):
    if (board[0]==player and board[1]==player and board[2]==player):
        return True
    elif (board[3]==player and board[4]==player and board[5]==player):
        return True
    elif (board[6]==player and board[7]==player and board[8]==player):
        return True
    elif (board[0]==player and board[3]==player and board[6]==player):
        return True
    elif (board[1]==player and board[4]==player and board[7]==player):
        return True
    elif (board[2]==player and board[5]==player and board[8]==player):
        return True
    elif (board[0]==player and board[4]==player and board[8]==player):
        return True
    elif (board[2]==player and board[4]==player and board[6]==player):
        return True
    else:
        return False
    pass

def new_game():
    print("Tic-tac-toe \nEnter number to place your piece in that location\n")
    board = new_board()
    show_board(board)
    next_turn(1, board)
    pass

new_game()



