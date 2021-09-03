game = [
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1]
]


def print_board():
    for x_axis in game:
        print(x_axis)


def white_move(x, y, l_or_r):
    piece = game[y][x]
    print(piece)
    if piece != 1:
        print("woah that's not even your piece")
        return
    if l_or_r == 0:
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
            print("Hey that's your own tm8")
            return
        elif space == 2:
            print("Checking for jump!")
            if y - 1 == 0 or x - 1 == 0:
                print("Woah if you jumped that player you would be off the board!")
                return
            jump_space = game[y - 2][x - 2]


print_board()
white_move(1, 5, 0)
print_board()
