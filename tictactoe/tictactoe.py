"""
Tic Tac Toe Player
"""

import math

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
    x_num = sum(row.count(X) for row in board)
    o_num = sum(row.count(O) for row in board)
    return X if x_num == o_num else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ava_operate = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                ava_operate.add((row, col))
    return ava_operate

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row.copy() for row in board]
    chess = player(board)
    row, col = action
    if row not in range(3) or col not in range(3):
        raise Exception
    if new_board[row][col] is not None:
        raise Exception
    new_board[row][col] = chess
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None: return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != None: return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != None: return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None: return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # 分别检查三列，三行，两个对角线，以及是否填满
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return True
        if board[0][i] == board[1][i] == board[2][i] != None:
            return True
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    for line in [diag1, diag2]:
        if len(set(line)) == 1 and line[0] is not None:
            return True
    is_full = True
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                is_full = False
    return True if is_full else False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        if v == -1:
            break
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        if v == 1:
            break
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    cur_player = player(board)
    best_act = None
    if cur_player == X:
        v = -math.inf
        for action in actions(board):
            score = min_value(result(board, action))
            if score > v:
                v = score
                best_act = action
            if v == 1:
                break
    else:
        v = math.inf
        for action in actions(board):
            score = max_value(result(board, action))
            if score < v:
                v = score
                best_act = action
            if v == -1:
                break
    return best_act
    
