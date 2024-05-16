"""
Tic Tac Toe Player
"""

import math
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
    x = 0
    o = 0
    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1

    if x == o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    n_actions = set()
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == EMPTY:
                n_actions.add((i, j))

    return n_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp_board = copy.deepcopy(board)

    if temp_board[action[0]][action[1]] != EMPTY:
        raise Exception("Wrong position")
    else:
        temp_board[action[0]][action[1]] = player(board)

    return temp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def check(letter):

        cols = len(board[0])
        for i in range(cols):
            if board[0][i] == board[1][i] == board[2][i] == letter:
                return True

        for i in board:
            if all(element == letter for element in i):
                return True

        if board[0][0] == board[1][1] == board[2][2] == letter:
            return True

        if board[0][2] == board[1][1] == board[2][0] == letter:
            return True

        return False

    if check(X):
        return X
    elif check(O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    rows = len(board)
    cols = len(board[0])

    if winner(board) == X or winner(board) == O:
        return True

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(s):
        if terminal(s):
            return utility(s)
        v = math.inf
        for z in actions(s):
            v = min(v, min_value(result(s, z)))
        return v

    def min_value(s):
        if terminal(s):
            return utility(s)
        v = -math.inf
        for z in actions(s):
            v = max(v, max_value(result(s, z)))
        return v

    if terminal(board):
        return None

    o_action = tuple()

    if player(board) == O:
        for i in actions(board):
            k = min_value(result(board, i))
            if k == -1:
                return i
            elif k == 0:
                o_action = i

        return o_action
    else:
        for i in actions(board):
            k = max_value(result(board, i))
            if k == 1:
                return i
            elif k == 0:
                o_action = i

        return o_action


