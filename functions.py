def play(gameboard, player, row_choice, col_choice):
    if(gameboard[row_choice][col_choice] == 0):
        try:
            gameboard[row_choice][col_choice] = player
            return True, gameboard
        except IndexError:
            print("Pls inform Something between 0 and 2\n")
        except:
            print("Something went wrong!\n")
    else:
        print("This spot is not available!\n")
    return False, gameboard

def print_gameboard(gameboard):
    for row in gameboard:
        print(row)

def check_win(gameboard):
    for row in gameboard:
        if(check_equal(row)):
            print("Horizontal winner!")
            return True

    return False

def check_equal(list):
    list = iter(list)
    try:
        first = next(list)
    except StopIteration:
        return True
    return all(first != 0 and first == rest for rest in list)