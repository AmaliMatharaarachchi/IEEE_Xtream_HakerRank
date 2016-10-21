n = input()
board = []
game_board = {}

# -------------------
if n % 2 == 1:
    for i in range(n):
        if i % 2 == 0:
            board[0:0] = list(raw_input())
        else:
            board[0:0] = reversed(list(raw_input()))
else:
    for i in range(n):
        if i % 2 == 1:
            board[0:0] = list(raw_input())
        else:
            board[0:0] = reversed(list(raw_input()))


# ---------------------

m = input()
players = {}

for i in range(m):
    players[i] = -1
loop = True
val = 0
# -----------------------

def game_board_pos(position, i, players, count):
    if count >3:
        print "PLAYER", i + 1, "WINS BY EVIL CYCLE!"
        return -10
    else:
        if (position not in players.values()):
            return game_board[position]
        else:
            while ((position in players.values())):
                position += 1

            return game_board_pos(game_board[position], i, players, count + 1)


# ----------get snake and bunny values to board--------

for i in range(len(board)):
    # bunnies
    if board[i].isdigit():
        if (board[i:].count(board[i]) == 2):
            temp = board[i]
            board.remove(board[i])
            index = board.index(temp) + 1
            board.insert(i, temp)
            game_board[i] = index
            game_board[index] = index

    # snakes
    elif board[i].isalpha():
        if (board[i:].count(board[i]) == 2):
            temp = board[i]
            board.remove(board[i])
            index = board.index(temp) + 1
            board.insert(i, temp)
            game_board[index] = i

            game_board[i] = i
    else:
        if not (game_board.has_key(i)):
            game_board[i] = i

# we have dict[current:next]
# ------------------------------------


while (loop):
    for i in range(m):
        if loop:
            d1 = input()
            d2 = input()
            tt=players[i] + d1 + d2
            if (tt <= n * n - 1):
                position = game_board[tt]

                del players[i]
                val = game_board_pos(position, i, players, 0)

                if (val == -10):
                    loop=False
                else:
                    players[i] = val

                if (d1 == d2):
                    d1 = input()
                    tt=players[i] + d1
                    if (tt <= n * n - 1):
                        position = game_board[tt]

                        val = game_board_pos(position, i, players, 0)
                        if (val == -10):
                            loop=False
                        else:
                            players[i] = val
                    else:
                        loop=False
                if players[i] >= (n * n) - 1:
                    loop = False
                print players
            else:
                loop=False
if val != -10:
    for i in players.values():
        print i + 1,
