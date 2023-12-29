"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player_x = 0
    player_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                player_x += 1
            elif cell == O:
                player_o += 1
            # end if
        # end for
    # end for

    if player_x > player_o:
        return O
    # end if
    return X
# end def


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    positions = set()
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == EMPTY:
                positions.add((i, j))
            # end if
        # end for
    # end for
    return positions
# end def


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action or len(action) != 2:
        raise Exception("Invalid action")
    # end if

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy
# end def


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    N = len(board)   # as board is NxN sized
    X_win = [X]*N
    O_win = [O]*N

    # checking row-wise for winner
    for row in board:
        if X_win == row:
            return X
        elif O_win == row:
            return O
        # end if
    # end for

    # checking column-wise for winner
    for i in range(N):
        col = [board[x][i] for x in range(N)]
        if X_win == col:
            return X
        elif O_win == col:
            return O
        # end if
    # end for

    # checking diagonal for winner
    diagonal_1 = []
    diagonal_2 = []
    for i in range(N):
        diagonal_1.append(board[i][i])
        diagonal_2.append(board[i][N-i-1])
    # end for
    if X_win == diagonal_1 or X_win == diagonal_2:
        return X
    elif O_win == diagonal_1 or O_win == diagonal_2:
        return O
    # end if

    return None
# end def


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    # end if

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
            # end if
        # end for
    # end for
    return True
# end def


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    # end if
    return 0
# end def


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # end if

    p = player(board)
    p_action = None
    if p == X:  # try to maximize for X player
        max_value = -100
        for action in actions(board):
            r = minimize(result(board, action))
            if r > max_value:
                max_value = r
                p_action = action
            # end if
        # end for

    else:   # try to minimize for O player
        min_value = 100
        for action in actions(board):
            r = maximize(result(board, action))
            if r < min_value:
                min_value = r
                p_action = action
            # end if
        # end for
    # end if
    return p_action
# end def


def maximize(board):
    if terminal(board):
        return utility(board)
    # end if

    v = -100
    for action in actions(board):
        v = max(v, minimize(result(board, action)))
    # end for
    return v
# end def


def minimize(board):
    if terminal(board):
        return utility(board)
    # end if

    v = 100
    for action in actions(board):
        v = min(v, maximize(result(board, action)))
    # end for
    return v
# end def
