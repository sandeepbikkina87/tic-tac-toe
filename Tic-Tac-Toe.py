import numpy as np
import random
from time import sleep
#creating an empty tic-tac-toe  board
def empty_board():
    board=np.array([
                    [0,0,0],
                    [0,0,0],
                    [0,0,0]
                    ])
    return(board)
#check for empty places on the tic-tac-toe Board
def empty_places(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                l.append((i,j))
    return(l)
#select a random place for the player on the tic tac toe board
def random_place(board,player):
    select=empty_places(board)
    current_location=random.choice(select)
    board[current_location]=player
    return(board)
#checks whether the player has three of their marks in a horizontal row
def row_winner(board,player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
            if board[x,y]!=player:
                win=False
                continue
        if win==True:
            return(win)
    return(win)
#checks whether the player has three of their marks in a vertical row
def col_winner(board,player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
            if board[x,y]!=player:
                win=False
                continue
        if win==True:
            return(win)
    return(win)
#check the diagnal rows for a winner
def diag_winner(board,player):
    win=True
    y=0
        
    for x in range(len(board)):
        if board[x,x]!=player:
            win=False
    if win:
        return win
    win=True
    if win:
        for x in range(len(board)):
            y=len(board)-1-x
            if board[x,y]!=player:
                win=False
    return(win)
#Evaluate whether there is a winner or a tie.
def evaluate_game(board):
    #winner[0=indecisive; 1=player; 2=player; -1=tie]
    winner=0
    for player in[1,2]:
        if (row_winner(board,player)or
            col_winner(board,player)or
            diag_winner(board,player)):
           winner=player
    if np.all(board!=0) and winner==0:
        winner=-1
    return winner
def tic_tac_toe():
    board=empty_board()
    winner=0
    counter=1
    print(board)
    sleep(2)
    while winner==0:
        for player in[1,2]:
            brd=random_place(board,player)
            print("Board after"+str(counter)+"move")
            print(brd)
            sleep(2)
            counter+=1
            winner=evaluate_game(brd)
            if winner!=0:
                break
    return(winner)
print("Winner is player:"+str(tic_tac_toe()))