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
    count_X = 0
    count_O = 0
    for row in board:
        for col in row:
            if col == X:
                count_X += 1
            if col == O:
                count_O += 1
            else:
                pass
    if count_X > count_O:
        return O
    if count_O > count_X:
        return X
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                options.add((i, j))
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Move not valid.")
    
    if action[0] not in [0, 1, 2]:
        raise Exception("Move not valid.")

    if action[1] not in [0, 1, 2]:
        raise Exception("Move not valid.")

    try:
        initial_state = copy.deepcopy(board)
        initial_state[action[0]][action[1]] = player(board)
        return initial_state
    except:
        print("An exception ocurred.")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == X:
                return X
            if board[0][col] == O:
                return O
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        if board[0][0] == O:
            return O
            
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return X
        if board[0][2] == O:
            return O
    
    return None     


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        best = float("-inf")
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best:
                best = value
                move = action

    else:
        best = float("inf")
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best:
                best = value
                move = action

    return move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v