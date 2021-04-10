# ✅

from point import Point

EMPTY = '.'

def one_step_front(board, cur_pos:Point('x', 'y'), color):
    if 0 <= cur_pos.x + 1 <= 7:
        if board[cur_pos.x + 1][cur_pos.y] == EMPTY or board[cur_pos.x + 1][cur_pos.y].color != color:
                return [Point(cur_pos.x + 1, cur_pos.y)]

def one_step_back(board, cur_pos:Point('x', 'y'), color):
    if 0 <= cur_pos.x - 1 <= 7:
        if board[cur_pos.x - 1][cur_pos.y] == EMPTY or board[cur_pos.x - 1][cur_pos.y].color != color:
            return [Point(cur_pos.x - 1, cur_pos.y)]


def front(board, cur_pos:Point('x', 'y'), color): 
    """
    Takes current position as input and returns available forward moves 
    """
    moves = []
    for i in range(cur_pos.x + 1, 8):
        moves.append(Point(i, cur_pos.y))
        if board[i][cur_pos.y] != EMPTY:
            if board[i][cur_pos.y].color == color:
                moves.pop()
            break
    return moves


def back(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available backward moves 
    """
    moves = []
    for i in range(cur_pos.x - 1, -1, -1):
        moves.append(Point(i, cur_pos.y))
        if board[i][cur_pos.y] != EMPTY:
            if board[i][cur_pos.y].color == color:
                moves.pop()
            break
    return moves


def one_step_right(board, cur_pos:Point('x', 'y'), color):
    if 0 <= cur_pos.y + 1 <= 7:
        if board[cur_pos.x][cur_pos.y + 1] == EMPTY or board[cur_pos.x][cur_pos.y + 1].color != color:
            return [Point(cur_pos.x, cur_pos.y + 1)]


def one_step_left(board, cur_pos:Point('x', 'y'), color):
    if 0 <= cur_pos.y - 1 <= 7:
        if board[cur_pos.x][cur_pos.y - 1] == EMPTY or board[cur_pos.x][cur_pos.y - 1].color != color:
            return [Point(cur_pos.x, cur_pos.y - 1)]


def right(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available right-side moves 
    """
    moves = []
    for i in range(cur_pos.y + 1, 8):
        moves.append(Point(cur_pos.x, i))
        if board[cur_pos.x][i] != EMPTY:
            if board[cur_pos.x][i].color == color:
                moves.pop()
            break
    return moves


def left(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available left-side moves 
    """
    moves = []
    for i in range(cur_pos.y - 1, -1, -1):
        moves.append(Point(cur_pos.x, i))
        if board[cur_pos.x][i] != EMPTY:
            if board[cur_pos.x][i].color == color:
                moves.pop()
            break
    return moves


def one_step_diag_right_forward(board, cur_pos:Point('x', 'y'), color):
    x = cur_pos.x + 1
    y = cur_pos.y + 1
    if 0 <= x <= 7 and 0 <= y <= 7:
        if board[x][y] == EMPTY or board[x][y].color != color:
            return [Point(x, y)]


def diag_right_forward(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available diagonally-right-side-forward moves 
    """
    moves = []
    x = cur_pos.x + 1
    y = cur_pos.y + 1
    while 0 <= x <= 7 and 0 <= y <= 7:
        moves.append(Point(x, y))
        if board[x][y] != EMPTY:
            if board[x][y].color == color:
                moves.pop()
            break
        x += 1
        y += 1
    return moves


def one_step_diag_right_backward(board, cur_pos:Point('x', 'y'), color):
    x = cur_pos.x - 1
    y = cur_pos.y + 1
    if 0 <= x <= 7 and 0 <= y <= 7:
        if board[x][y] == EMPTY or board[x][y].color != color:
            return [Point(x, y)]


def diag_right_backward(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available diagonally-right-side-backward moves 
    """
    moves = []
    x = cur_pos.x - 1
    y = cur_pos.y + 1
    while 0 <= x <= 7 and 0 <= y <= 7:
        moves.append(Point(x, y))
        if board[x][y] != EMPTY:
            if board[x][y].color == color:
                moves.pop()
            break
        x -= 1
        y += 1
    return moves


def one_step_diag_left_forward(board, cur_pos:Point('x', 'y'), color):
    x = cur_pos.x + 1
    y = cur_pos.y - 1
    if 0 <= x <= 7 and 0 <= y <= 7:
        if board[x][y] == EMPTY or board[x][y].color != color:
            return [Point(x, y)]


def diag_left_forward(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available diagonally-left-side-forward moves 
    """
    moves = []
    x = cur_pos.x + 1
    y = cur_pos.y - 1
    while 0 <= x <= 7 and 0 <= y <= 7:
        moves.append(Point(x, y))
        if board[x][y] != EMPTY:
            if board[x][y].color == color:
                moves.pop()
            break
        x += 1
        y -= 1
    return moves


def one_step_diag_left_backward(board, cur_pos:Point('x', 'y'), color):
    x = cur_pos.x - 1
    y = cur_pos.y - 1
    if 0 <= x <= 7 and 0 <= y <= 7:
        if board[x][y] == EMPTY or board[x][y].color != color:
            return [Point(x, y)]


def diag_left_backward(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available diagonally-left-side-backward moves 
    """
    moves = []
    x = cur_pos.x - 1
    y = cur_pos.y - 1
    while 0 <= x <= 7 and 0 <= y <= 7:
        moves.append(Point(x, y))
        if board[x][y] != EMPTY:
            if board[x][y].color == color:
                moves.pop()
            break
        x -= 1
        y -= 1
    return moves


def L_front(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available L-shape forward moves 
    """
    moves = []
    if 0 <= cur_pos.x + 1 <= 7:
        if 0 <= cur_pos.y + 2 <= 7:
            if board[cur_pos.x + 1][cur_pos.y + 2] == EMPTY or board[cur_pos.x + 1][cur_pos.y + 2].color != color:
                moves.append(Point(cur_pos.x + 1, cur_pos.y + 2))
        if 0 <= cur_pos.y - 2 <= 7:
            if board[cur_pos.x + 1][cur_pos.y - 2] == EMPTY or board[cur_pos.x + 1][cur_pos.y - 2].color != color:
                moves.append(Point(cur_pos.x + 1, cur_pos.y - 2)) 
    if 0 <= cur_pos.x + 2 <= 7:
        if 0 <= cur_pos.y + 1 <= 7:
            if board[cur_pos.x + 2][cur_pos.y + 1] == EMPTY or board[cur_pos.x + 2][cur_pos.y + 1].color != color:
                moves.append(Point(cur_pos.x + 2, cur_pos.y + 1))
        if 0 <= cur_pos.y - 1 <= 7:
            if board[cur_pos.x + 2][cur_pos.y - 1] == EMPTY or board[cur_pos.x + 2][cur_pos.y - 1].color != color:
                moves.append(Point(cur_pos.x + 2, cur_pos.y - 1))
    return moves


def L_back(board, cur_pos:Point('x', 'y'), color):
    """
    Takes current position as input and returns available L-shape backward moves 
    """
    moves = []
    if 0 <= cur_pos.x - 1 <= 7:
        if 0 <= cur_pos.y + 2 <= 7:
            if board[cur_pos.x - 1][cur_pos.y + 2] == EMPTY or board[cur_pos.x - 1][cur_pos.y + 2].color != color:
                moves.append(Point(cur_pos.x - 1, cur_pos.y + 2))
        if 0 <= cur_pos.y - 2 <= 7:
            if board[cur_pos.x - 1][cur_pos.y - 2] == EMPTY or board[cur_pos.x - 1][cur_pos.y - 2].color != color:
                moves.append(Point(cur_pos.x - 1, cur_pos.y - 2)) 
    if 0 <= cur_pos.x - 2 <= 7:
        if 0 <= cur_pos.y + 1 <= 7:
            if board[cur_pos.x - 2][cur_pos.y + 1] == EMPTY or board[cur_pos.x - 2][cur_pos.y + 1].color != color:
                moves.append(Point(cur_pos.x - 2, cur_pos.y + 1))
        if 0 <= cur_pos.y - 1 <= 7:
            if board[cur_pos.x - 2][cur_pos.y - 1] == EMPTY or board[cur_pos.x - 2][cur_pos.y - 1].color != color:
                moves.append(Point(cur_pos.x - 2, cur_pos.y - 1))
    return moves


# Special rules for pawns:
def pawn_rules(board, cur_pos, color, init):
    available_moves = []
    if color == 'B':
        if not init:
            if board[cur_pos.x + 1][cur_pos.y] == EMPTY and board[cur_pos.x + 2][cur_pos.y] == EMPTY:
                available_moves.append(Point(cur_pos.x + 2, cur_pos.y))
        if 0 <= cur_pos.x + 1 <= 7:
            if board[cur_pos.x + 1][cur_pos.y] == EMPTY:
                available_moves.append(Point(cur_pos.x + 1, cur_pos.y))
            if 0 <= cur_pos.y + 1 <= 7 and board[cur_pos.x + 1][cur_pos.y + 1] != EMPTY and board[cur_pos.x + 1][cur_pos.y + 1].color != color:
                available_moves.append(Point(cur_pos.x + 1, cur_pos.y + 1))
            if 0 <= cur_pos.y - 1 <= 7 and board[cur_pos.x + 1][cur_pos.y - 1] != EMPTY and board[cur_pos.x + 1][cur_pos.y - 1].color != color:
                available_moves.append(Point(cur_pos.x + 1, cur_pos.y - 1))
    elif color == 'W':
        if not init:
            if board[cur_pos.x - 1][cur_pos.y] == EMPTY and board[cur_pos.x - 2][cur_pos.y] == EMPTY:
                available_moves.append(Point(cur_pos.x - 2, cur_pos.y))
        if 0 <= cur_pos.x - 1 <= 7:
            if board[cur_pos.x - 1][cur_pos.y] == EMPTY:
                available_moves.append(Point(cur_pos.x - 1, cur_pos.y))
            if 0 <= cur_pos.y + 1 <= 7 and board[cur_pos.x - 1][cur_pos.y + 1] != EMPTY and board[cur_pos.x - 1][cur_pos.y + 1].color != color:
                available_moves.append(Point(cur_pos.x - 1, cur_pos.y + 1))
            if 0 <= cur_pos.y - 1 <= 7 and board[cur_pos.x - 1][cur_pos.y - 1] != EMPTY and board[cur_pos.x - 1][cur_pos.y - 1].color != color:
                available_moves.append(Point(cur_pos.x - 1, cur_pos.y - 1))
    return available_moves