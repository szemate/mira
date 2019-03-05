board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

player = 'o'

while True:
    ######################
    # Announce the player

    print()
    print("------------------------")
    print()
    print("NEXT ROUND: '", player, "'")
    print()

    ##################
    # Print the board

    print("    0   1   2   ")
    row = 0
    while row <= 2:
        column = 0
        line = str(row) + " | "
        while column < 3:
            line = line + board[row][column] + " | "
            column = column + 1
        print("  +---+---+---+ ")
        print(line)
        row = row + 1
    print("  +---+---+---+ ")
    print()

    ##################################
    # Find out if anyone won the game

    # 1. The same sign in all 3 cells of a row

    row = 0
    while row <= 2:
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            print()
            print("THE WINNER IS '", board[row][0], "' !!!")
            exit()
        row = row + 1

    # 2. The same sign in all 3 cells of a column

    column = 0
    while column <= 2:
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != " ":
            print()
            print("THE WINNER IS '", board[0][column], "' !!!")
            exit()
        column = column + 1

    # 3. The same sign in either of the diagonals

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        print()
        print("THE WINNER IS '", board[0][0], "' !!!")
        exit()

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        print()
        print("THE WINNER IS '", board[0][2], "' !!!")
        exit()

    # 4. The board is full

    is_all_filled = True
    row = 0
    while row <= 2:
        column = 0
        while column < 3:
            if board[row][column] == ' ':
                is_all_filled = False
            column = column + 1
        row = row + 1

    if is_all_filled:
        print()
        print("IT IS A DRAW!!!")
        exit()

    ####################################
    # Put a new 'x' or 'o' on the board

    new_row = int(input("Row: "))
    new_column = int(input("Column: "))

    # Check if the new location is valid
    if new_row <= 2 and new_column <= 2 and board[new_row][new_column] == " ":
        # Put the 'x' or 'o' on the board
        board[new_row][new_column] = player

        # Switch players
        if player == 'o':
            player = 'x'
        else:
            player = 'o'
