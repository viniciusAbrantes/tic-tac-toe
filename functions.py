def play(gameboard, player, row_choice, col_choice):
    try:
        if(gameboard[row_choice][col_choice] == 0):
            gameboard[row_choice][col_choice] = player
            return True, gameboard
        else:
            print("This spot is not available!\n")
    except IndexError:
        print("Please inform Something between 0 and 2\n")
    except:
        print("Something went wrong!\n")

    return False, gameboard

def print_gameboard(gameboard):
    print("   " + "  ".join([str(i) for i in range(len(gameboard))]))
    for count, row in enumerate(gameboard):
        print(count,row)

def check_win(gameboard):
    #Horizontal
    for row in gameboard:
        if(check_equal(row)):
            print_gameboard(gameboard)
            print("Player %s won horizontally!" % (row[0]))
            return True

    #Vertical
    for i in range(len(gameboard)):
        vertical = []
        for row in gameboard:
            vertical.append(row[i])
        if(check_equal(vertical)):
            print_gameboard(gameboard)
            print("Player %s won vertically!" % (vertical[0]))
            return True

    #Diagonal
    main_diag = []
    for i, row in enumerate(gameboard):
        main_diag.append(row[i])
    if(check_equal(main_diag)):
        print_gameboard(gameboard)
        print("Player %s won diagonally!" % (main_diag[0]))
        return True

    sec_diag = []
    i = reversed(range(len(gameboard)))
    for row in gameboard:
        sec_diag.append(row[next(i)])
    if(check_equal(sec_diag)):
        print_gameboard(gameboard)
        print("Player %s won diagonally!" % (sec_diag[0]))
        return True
    return False

def check_draw(gameboard):
    for row in gameboard:
        if row.count(0) != 0:
            return False
    print("We have no winner... bye bye!")
    return True

def check_equal(list):
    if list.count(list[0]) == len(list) and list[0] != 0:
        return True
    else:
        return False