'''
Project 2 - Shut The Box - Fall 2025  
Author: Lamiek Haile lamiek

This program simulates the single-player game Shut The Box.
The player rolls two dice and eliminates numbers from 1–9 that
sum to the dice roll. The goal is to eliminate all numbers before
no valid moves remain.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Lamiek haile
'''

import random
from project2_fcn import can_play



def print_board(board, dice1, dice2):
    ''' This function prints the board and the dice values rolled. 
        It takes the current board, the first dice, and the second dice as parameters. 
        It does not return anything. '''
    for i in board:
        if i == 0:
            print('-', end = ' ')
        else:
            print(i, end = ' ')
    
    print()
    print('dice1 =', dice1)
    print('dice2 =', dice2)
    
def get_input():
    ''' This function gets the user's numbers to eliminate. 
        It does not take any parameters and returns a list of integers entered by the user. '''
    user_input = input('Enter the numbers you want to eliminate (separated by spaces): ')
    
    ints = [int(i) for i in user_input.split()]
    
    return ints

def check_input(user_input, board, total):
    ''' This function checks if the user's input is valid. 
        It takes the user's input, the current board, and the total of both dice as parameters. 
        It returns True if the input is valid and False if it is not. '''
    nums = sum(user_input)
    
    if nums != total:
        print(f"Error: The sum of {user_input} does not equal {total}")
        return False
    for i in user_input:
        if i not in board:
            print(f'Error: {i} is not on the board')
            return False
    num = board.copy()
    
    for i in user_input:
        if i in num:
            num.remove(i)
        else:
            print('Error: You cannot enter the same number twice.')
            return False
        
    return True

def main():
    ''' This function runs the main game of Shut The Box. 
        It does not take any parameters and does not return anything.
    '''
    board = [1,2,3,4,5,6,7,8,9]
    
    print("Welcome to Shut The Box")
    
    while True:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2
        
        print_board(board,dice1,dice2)
        
        if not can_play(board, dice1, dice2):
            print("You have no moves left!\nBetter luck next time!")
            break
        
        user_input = get_input()
        while not check_input(user_input, board, total):
            user_input = get_input()
            
        for num in user_input:
            index = board.index(num)
            board[index] = 0
            
        if sum(board) == 0:
            print_board(board, dice1, dice2)
            print("You Shut The Box!")
            break
    
    
if __name__ == '__main__':
    main()
    
            


    
    



