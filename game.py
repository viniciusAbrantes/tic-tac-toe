def play(gameboard, player, row_choice, col_choice):
    gameboard[row_choice][col_choice] = player
    
    #Verify if it has a winner
    #TODO

    return gameboard

def print_gameboard(gameboard):
    for row in gameboard:
        print(row)

game_size = int(input("Inform the gameboard size: "))

gameboard = []
for i in range(game_size):
    row = []
    for col in range(game_size):
        row.append(0)
    gameboard.append(row)

gameboard = play(gameboard, 1, 0, 0)
print_gameboard(gameboard)