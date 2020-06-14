import numpy as npy
import pygame
import sys
import math

ROWLENGTH=6
COLUMNLENGTH=8
LENGTHOFBOX=100

def getboard(row,col):
    board=npy.zeros((row,col))
    return board

def valid_location(board,input):
    return board[ROWLENGTH-1][int(input)] == 0

def add_piece_to_board(board,input,player):
    row=0
    while board[int(row)][int(input)] != 0:
        row=row+1
    board[int(row)][int(input)]=player
    return int(row)

def check_if_won(board,temprow,tempcol):
    row=int(temprow)
    col=int(tempcol)
    if row-3>=0 and board[row][col]==board[row-1][col] and board[row][col]==board[row-2][col] and board[row][col]==board[row-3][col]:
        return True
    
    index=1
    num=1
    while num<=3 and index<=3 and col-index>=0 and board[row][col]==board[row][col-index]:
        num=num+1
        index=index+1
    
    index=1
    while num<=3 and col+index<=COLUMNLENGTH-1 and board[row][col]==board[row][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True
    
    index=1
    num=1
    while num<=3 and row-index>=0 and col-index>=0 and board[row][col]==board[row-index][col-index]:
        num=num+1
        index=index+1

    index=1
    while num<=3 and row+index<=ROWLENGTH-1 and col+index<=COLUMNLENGTH-1 and board[row][col]==board[row+index][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True
    
    index=1
    num=1
    while num<=3 and row+index<=ROWLENGTH-1 and col-index>=0 and board[row][col]==board[row+index][col-index]:
        num=num+1
        index=index+1
    
    index=1
    while num<=3 and row-index>=0 and col+index<=COLUMNLENGTH-1 and board[row][col]==board[row-index][col+index]:
        num=num+1
        index=index+1

    if num>3:
        return True

    return False
    
def draw_board(board):
    for row in range(ROWLENGTH):
        for col in range(COLUMNLENGTH):
            pygame.draw.rect(screen,(0,0,255),(col*LENGTHOFBOX,(row+1)*LENGTHOFBOX, (col+1)*LENGTHOFBOX, (row+2)*LENGTHOFBOX)) 
            pygame.draw.circle(screen,(0,0,0),(int(col*LENGTHOFBOX+LENGTHOFBOX/2),int((row+1)*LENGTHOFBOX+LENGTHOFBOX/2)),int(LENGTHOFBOX/2-5))

    for row in range(ROWLENGTH):
        for col in range(COLUMNLENGTH):
            if(board[row][col]==1):
                pygame.draw.circle(screen,(255,0,0),(int(col*LENGTHOFBOX+LENGTHOFBOX/2),int((ROWLENGTH+1)*LENGTHOFBOX-(row+1)*LENGTHOFBOX+LENGTHOFBOX/2)),int(LENGTHOFBOX/2-5))
            elif(board[row][col]==2):
                pygame.draw.circle(screen,(0,255,0),(int(col*LENGTHOFBOX+LENGTHOFBOX/2),int((ROWLENGTH+1)*LENGTHOFBOX-(row+1)*LENGTHOFBOX+LENGTHOFBOX/2)),int(LENGTHOFBOX/2-5))
    
    pygame.display.update()

board = getboard(ROWLENGTH,COLUMNLENGTH)
someone_won = False
turn = 1

pygame.init()
height=(ROWLENGTH+1)*LENGTHOFBOX
width=(COLUMNLENGTH)*LENGTHOFBOX
size=(width,height)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

font=pygame.font.SysFont("comicsansms", 70)

while not someone_won:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit
        
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
            position=event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen,(255,0,0),(position,int(LENGTHOFBOX/2)),int(LENGTHOFBOX/2))
            elif turn == 2:
                pygame.draw.circle(screen,(0,255,0),(position,int(LENGTHOFBOX/2)),int(LENGTHOFBOX/2))
        
        pygame.display.update()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if turn == 1:
                position=event.pos[0]
                user_input=int(math.floor(position/LENGTHOFBOX))

                if valid_location(board,user_input):
                    row=add_piece_to_board(board,user_input,1)
                    if check_if_won(board,row,user_input):
                        pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                        label=font.render("PLAYER 1 WINS",1,(255,0,0))
                        screen.blit(label, (40,0))
                        someone_won=True


            else:
                position=event.pos[0]
                user_input=int(math.floor(position/LENGTHOFBOX))

                if valid_location(board,user_input):
                    row=add_piece_to_board(board,user_input,2)
                    if check_if_won(board,row,user_input):
                        pygame.draw.rect(screen,(0,0,0),(0,0,COLUMNLENGTH*LENGTHOFBOX,LENGTHOFBOX))
                        label=font.render("PLAYER 2 WINS",1,(0,255,0))
                        screen.blit(label, (40,0))
                        someone_won=True

            draw_board(board)

            if turn == 1:
                turn=2
            else:
                turn=1
        
    if someone_won:
        pygame.time.wait(5000)
