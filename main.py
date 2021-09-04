game = [
    [2, 0, 2, 0, 2, 0, 2, 0],  # /\
    [0, 2, 0, 2, 0, 2, 0, 2],  # || up is -
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],  # -> is +
    [0, 0, 0, 0, 0, 0, 0, 0],  # <- is -
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],  # ||
    [0, 1, 0, 1, 0, 1, 0, 1]   # \/ down is +
]


def print_board_white():
    x = 0
    for x_axis in game:
        y = 0
        string1 = ""
        for coord in x_axis:
            if coord == 0:
                if ((x + y) % 2) == 0:
                    string1 += " # "
                else:
                    string1 += " 🟫"
            elif coord == 1:
                string1 += " ⚪ "
            elif coord == 2:
                string1 += " 🔴 "
            y += 1
        print(string1)
        x += 1


def print_board_black():
    game.reverse()
    x = 0
    for x_axis in game:
        y = 0
        string1 = ""
        x_axis.reverse()
        for coord in x_axis:
            if coord == 0:
                if ((x + y) % 2) == 0:
                    string1 += " - "
                else:
                    string1 += "🟫"
            elif coord == 1:
                string1 += " ⚪ "
            elif coord == 2:
                string1 += " 🔴 "
            y += 1
        print(string1)
        x += 1
    game.reverse()


def white_move(x, y, direction):
    piece = game[y][x]
    print(piece)
    if piece != 1 and piece != 4:
        print("woah that's not even your piece")
        return
    if direction == 0:
        if x == 0 or y == 0:
            print("woah there you would be off the board with that move")
            return
        space = game[y - 1][x - 1]
        if space == 0:
            print("Valid move!")
            game[y][x] = 0
            game[y - 1][x - 1] = 1
            return

        elif space == 1:
            print("Hey that's your own piece")
            return
        elif space == 2:
            print("Checking for jump!")
            if y - 1 == 0 or x - 1 == 0:
                print("Woah if you jumped that player you would be off the board!")
                return
            jump_space = game[y - 2][x - 2]
            if jump_space == 0:
                print("That's a jump")
                game[y - 1][x - 1] = 0
                game[y][x] = 0
                game[y - 2][x - 2] = 1
                return
            else:
                print("you can't jump to somewhere an opposing piece is")
                return
        else:
            print("!!!ERROR!!!")
    if direction == 1:
        if x == 7 or y == 0:
            print("woah there you would be off the board with that move")
            return
        space = game[y - 1][x + 1]
        if space == 0:
            print("Valid move!")
            game[y][x] = 0
            game[y - 1][x + 1] = 1
            return

        elif space == 1:
            print("Hey that's your own piece")
            return
        elif space == 2:
            print("Checking for jump!")
            if y - 1 == 0 or x + 1 == 0:
                print("Woah if you jumped that player you would be off the board!")
                return
            jump_space = game[y - 2][x - 2]
            if jump_space == 0:
                print("That's a jump")
                game[y - 1][x + 1] = 0
                game[y][x] = 0
                game[y - 2][x + 2] = 1
                return
            else:
                print("you can't jump to somewhere a piece is")
                return
        else:
            print("!!!ERROR!!!")
    if piece != 2:
        print("Your not a king you can't go backwards")
        return
    if direction == 3:
        if x == 7 or y == 7:
            print("woah there you would be off the board with that move")
            return
        space = game[y + 1][x + 1]
        if space == 0:
            print("Valid move!")
            game[y][x] = 0
            game[y + 1][x + 1] = 1
            return

        elif space == 1:
            print("Hey that's your own piece")
            return
        elif space == 2:
            print("Checking for jump!")
            if y + 1 == 0 or x + 1 == 0:
                print("Woah if you jumped that player you would be off the board!")
                return
            jump_space = game[y + 2][x - 2]
            if jump_space == 0:
                print("That's a jump")
                game[y + 1][x + 1] = 0
                game[y][x] = 0
                game[y + 2][x + 2] = 1
                return
            else:
                print("you can't jump to somewhere a piece is")
                return
    if direction == 4:
        if x == 0 or y == 7:
            print("woah there you would be off the board with that move")
            return
        space = game[y + 1][x - 1]
        if space == 0:
            print("Valid move!")
            game[y][x] = 0
            game[y + 1][x - 1] = 1
            return

        elif space == 1:
            print("Hey that's your own piece")
            return
        elif space == 2:
            print("Checking for jump!")
            if y + 1 == 0 or x - 1 == 0:
                print("Woah if you jumped that player you would be off the board!")
                return
            jump_space = game[y + 2][x - 2]
            if jump_space == 0:
                print("That's a jump")
                game[y + 1][x - 1] = 0
                game[y][x] = 0
                game[y + 2][x - 2] = 1
                return
            else:
                print("you can't jump to somewhere a piece is")
                return


print_board_white()
white_move(1, 5, 0)
print_board_black()
