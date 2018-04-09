import random

game_on = False
playerNum = 0 

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

def change_board(board, playerIn):
    global playerNum
    if (playerNum==1):
        board[playerIn] = "X"
        pass
    elif (playerNum==2):
        board[playerIn] = "O"
        pass    
    show_board(board)
    return board 

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

def tie_check(board):
    tie = 0
    for a in range(len(board)):
        if (board[a]=="X" or board[a]=="O"):
            tie += 1
            pass
        pass
    if (tie==9):
        return True
    else:
        return False
    pass

def vs_bot(board):
    show_board(board)
    global playerNum
    global game_on
    while game_on == True:
        if playerNum == 1:
            #Player's turn
            while True:
                playerIn = int(input("Player "+str(playerNum)+"'s Turn\n"))
                if (board[playerIn]=="X" or board[playerIn]=="O"):
                    print("Position taken")
                    continue
                else:
                    break
            pass
        elif playerNum == 2:
            #Bot's turn
            print("Player "+str(playerNum)+"'s Turn\n")
            while True:
                playerIn = random.randint(0,8)
                if (board[playerIn]=="X" or board[playerIn]=="O"):
                    continue
                else:
                    break
            pass
        else:
            print("PlayerNum Error.")
            game_on = False
            new_game()
            pass
        next_turn(board, playerIn)
    pass

def vs_player(board):    
    show_board(board)
    global playerNum
    global game_on
    while game_on == True:
        while True:
            playerIn = int(input("Player "+str(playerNum)+"'s Turn\n"))
            if (board[playerIn]=="X" or board[playerIn]=="O"):
                print("Position taken")
                continue
            else:
                break
        pass
        next_turn(board, playerIn)
    pass

def next_turn(board, playerIn):
    global game_on
    board = change_board(board, playerIn)
    if (win_check("X", board)==True):
        print("Player One Wins\n")
        game_on = False
        new_game()
        pass
    elif (win_check("O", board)==True):
        print("Player Two Wins\n")
        game_on = False
        new_game()
        pass
    elif (tie_check(board)==True):
        print("Tie\n")
        game_on = False
        new_game()
        pass
    global playerNum
    if playerNum == 1:
        playerNum = 2
        pass
    elif playerNum == 2:
        playerNum = 1
        pass
    else:
        print("PlayerNum Error.")
        game_on = False
        new_game()
        pass
    pass

def new_game():
    global playerNum
    global game_on
    playerNum = 1
    game_on = True
    board = new_board()
    while True:
        choice = input("Enter 1 to play against a bot or 2 for a two-player game:\n")
        if choice == "1":
            vs_bot(board)
            break
        elif choice == "2":
            vs_player(board)
            break
        else:
            print("Invalid input.")
            continue
        pass
    pass

def main():    
    print("Tic-tac-toe \n")
    print("How to play:")
    print("Enter a number to place your piece in that location.\n")
    #print("Press Q anytime to quit.\n")
    print("Have fun!")
    new_game()
    pass

main() 
