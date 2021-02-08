# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:16:20 2020

@author: jonat
"""

def welcome_wagon():#receiving the input from the 2 players
    continue_playing=input
    continue_playing='yes'
    #ONE BIG WHILE FOR ALL OF IT
    while continue_playing =='yes':
        
        import collections
        import numpy as np
        inpt_lst=list()#VERIFYING NO DUPLICATION IN THE INT INPUTS
        board = [[' ',' ',' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        counter=0
        x=['X','X','X']
        o=['O','O','O']
        index=0
    

    
        
        
        print('welcome to tic tac toe!')
    
        #DECIDING SIDES AND WHO STARTS
        p1_xo_inpt=input('player 1 are you X or O?: ')#XO choice p1
        #saving_inputs(p1_xo_inpt)
    
        p1_input=input('player 1 will start. are you ready? enter yes or no: ')
        while p1_input=='no':
            p1_input=input('player 1 will start. are you ready? enter yes or no: ')
        
    
   
        #RECIEVING INPUT FROM PLAYER   
        p1_int_input=int(input('player 1 choose your position 1-9: '))
        inpt_lst.append(p1_int_input)
        build_board(p1_xo_inpt,p1_int_input,board,counter)
        while index <8:#the check if someone won
            
            #RECIEVING INPUT FROM PLAYER   
            p2_int_input=int(input('player 2 choose your position 1-9: '))
            index+=1
            for i in inpt_lst:
                while i==p2_int_input:
                    print('this value has already been enterd,try again')
                    p2_int_input=int(input('player 2 choose your position 1-9: '))
                    #build_board(p1_xo_inpt,p2_int_input)
                    #move to board display
            inpt_lst.append(p2_int_input)#checking no dupliction in input integars       
            counter+=1   
            build_board(p1_xo_inpt,p2_int_input,board,counter)
            #move to board display
            
            #CHECKING WIN IN 3 VERTICALY
            for elem in board: 
                if collections.Counter(elem) == collections.Counter(x) or collections.Counter(elem) == collections.Counter(o) : 
                    continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                    if continue_playing=='no':
                        print('LOOZZZZERS')
                        index=20
                        break
                          
                    else:
                        index=20#to get out of the inner while and start again
                        break
                
            #CHECKING WIN IN 3 DIAGNOLY
            if ((board[0][0]=='X') and(board[1][1]=='X') and (board[2][2]=='X')) or ((board[0][0]=='O') and (board[1][1]=='O') and (board[2][2]=='O')) :
                continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                if continue_playing=='no':
                    print('LOOZZZZERS')
                    index=20
                    break
                
                else:
                    break
            
            #CHECKING WIN IN 3 DIAGNOLY
            if ((board[2][0] == 'X') and (board[1][1] == 'X') and (board[0][2] == 'X')) or ((board[2][0]== 'O') and (board[1][1]== 'O') and (board[0][2] == 'O')) :
                continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                if continue_playing=='no':
                    print('LOOZZZZERS')
                    index=20
                    break
                          
                else:
                    break
                
                
            #CHECKING WIN IN 3 HORIZANTAL
            board_transpose = np.transpose(board) 
            #board_transpose = board.transpose()
            for elem in board_transpose: 
                if collections.Counter(elem) == collections.Counter(x) or collections.Counter(elem) == collections.Counter(o) : 
                    continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                    if continue_playing=='no':
                        print('LOOZZZZERS')
                        index=20
                        break
                          
                    else:
                        index=20#to get out of the inner while and start again
                        break
          
            
        
            #CHECKING IF SOMEONE HAS WON,OR NO ONE HAS WON  
            if index==20:  
                break
        
            elif index>=8: 
                continue_playing=input('no one has won, do you want to play again? ')#chcking if the player want to play again
                if continue_playing=='no':
                    print('LOOZZZZERS')
                    break
                
                else:
                    break

            #RECIEVING INPUT FROM PLAYER   
            p1_int_input=int(input('player 1 choose your position 1-9: '))
            index+=1
            for i in inpt_lst:
                while i==p1_int_input:
                    print('this value has already been enterd,try again')
                    p1_int_input=int(input('player 1 choose your position 1-9: '))
                    #build_board(p1_xo_inpt,p1_int_input)
                    #move to board display
            inpt_lst.append(p1_int_input)#checking no dupliction in input integars
            counter+=1
            build_board(p1_xo_inpt,p1_int_input,board,counter)
            #move to board display
        
            #CHECKING WIN IN 3 VERTICALY
            for elem in board: 
                if collections.Counter(elem) == collections.Counter(x) or collections.Counter(elem) == collections.Counter(o) : 
                    
                    continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                    if continue_playing=='no':
                        print('LOOZZZZERS')
                        index=20
                        break
                              
                    else:
                        index=20#to get out of the inner while and start again
                        break
                
        
            #CHECKING WIN IN 3 DIAGNOLY
            if ((board[0][0]=='X') and(board[1][1]=='X') and (board[2][2]=='X')) or ((board[0][0]=='O') and (board[1][1]=='O') and (board[2][2]=='O')) :
              
                continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                if continue_playing=='no':
                    print('LOOZZZZERS')
                    index=20
                    break
                          
                else:
                    break
        
            #CHECKING WIN IN 3 DIAGNOLY
            if ((board[2][0] == 'X') and (board[1][1] == 'X') and (board[0][2] == 'X')) or ((board[2][0]== 'O') and (board[1][1]== 'O') and (board[0][2] == 'O')) :
               
                continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                if continue_playing=='no':
                    print('LOOZZZZERS')
                    index=20
                    break
                          
                else:
                    break
                
                
            #CHECKING WIN IN 3 HORIZANTAL
            board_transpose = np.transpose(board) 
            #board_transpose = board.transpose()
            for elem in board_transpose: 
                if collections.Counter(elem) == collections.Counter(x) or collections.Counter(elem) == collections.Counter(o) : 
                    
                    continue_playing=input('you have won! do you want to play again? ')#chcking if the player want to play again
                    if continue_playing=='no':
                        print('LOOZZZZERS')
                        index=20
                        break
                          
                    else:
                        index=20#to get out of the inner while and start again
                        break
      
            #CHECKING IF SOMEONE HAS WON,OR NO ONE HAS WON  
            if index==20:  
                break
            
            elif index>=8: 
                continue_playing=input('no one has won, do you want to play again? ')#chcking if the player want to play again
                if continue_playing=='no':
                    print('LOOZZZZERS')
                    break
                
                else:
                    break

                
        


def build_board(p1_xo,inpt_int,board,counter):#i always need to use one variable in the func so i called it a variable ,because every time i call it, its in use of a different variable
    #lst_inputs=list()  #a list of the crucial inputs from the players,which i extract and peform the func on
    #lst_inputs.append(inputs)
    #lst_inputs.append(inputs)
    
    
    i=2
    j=0
    for k in range (1,10):#checks every possible input from the player and positions the x in the right place
        if k==inpt_int:
            if i>=0:
                if p1_xo=='x' or p1_xo=='X':
                    if counter%2==0:
                        board[i][j]='X'
                        display_board2(board)
                        continue
                    else:
                        board[i][j]='O'
                        display_board2(board)
                        continue
                else:
                    if counter%2==0:
                        board[i][j]='O'
                        display_board2(board)
                        continue
                    else:
                        board[i][j]='X'
                        display_board2(board)
                        continue
            else:
                break
        else:
            j+=1
            
        if j>2:
            i-=1
            j=0
            
        

from IPython.display import clear_output
clear_output()
def display_board2(board):
    #board = [[' ',' ',' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i, row in enumerate(board):
            for j, col in enumerate(row):
                print(col,end='')
                if (j<2):
                    print(" |",end='')
            if (i<2):
                print("\n--------")  
            else:
                print('\n')
                

welcome_wagon()

