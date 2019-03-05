from functions import *
from itertools import cycle

gameboard = [[0,0,0], [0,0,0], [0,0,0]]
#game_size = int(input("Inform the gameboard size: "))

players = cycle([1, 2])
game_over = False
while(not game_over):
    current_player = next(players)
    valid_choice = False
    while(not valid_choice):
        print_gameboard(gameboard)
        row_choice = int(input("Inform the row you wanna play: "))
        col_choice = int(input("Inform the column you wanna play: "))
        valid_choice, gameboard = play(gameboard, current_player, row_choice, col_choice)
        game_over = check_win(gameboard)