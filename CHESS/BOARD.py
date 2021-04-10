"""
Chess Game
"""
from movements import *
from point import Point
from copy import deepcopy
#####
import pygame

B=['Bking','Bqueen','Bbishop','Bpawn','Bknight','Brook']
Blacklist={'Bking':pygame.image.load("sprites/Bking.png"),
'Bqueen':pygame.image.load("sprites/Bqueen.png"),
'Bbishop':pygame.image.load("sprites/Bbishop.png"),
'Bpawn':pygame.image.load("sprites/Bpawn.png"),
'Brook':pygame.image.load("sprites/Brook.png"),          
'Bknight':pygame.image.load("sprites/Bknight.png")}
    
W=['Wking','Wqueen','Wbishop','Wpawn','Wknight','Wrook']
Whitelist={'Wking':pygame.image.load("sprites/Wking.png"),
'Wqueen':pygame.image.load("sprites/Wqueen.png"),
'Wbishop':pygame.image.load("sprites/Wbishop.png"),
'Wpawn':pygame.image.load("sprites/Wpawn.png"),
'Wrook':pygame.image.load("sprites/Wrook.png"),
'Wknight':pygame.image.load("sprites/Wknight.png")}

for i in B:
    Blacklist[i]=pygame.transform.scale(Blacklist[i],(54,54))

for j in W:
    Whitelist[j]=pygame.transform.scale(Whitelist[j],(54,54))

class BOARDCLASS(object):
    def __init__(self,win):
        self.draw(win)
    def draw(self,win):
        #print('running')
        for i in range(0,8):
            for j in range(0,8):
                if i%2==0:
                    if j%2==0:
                        pygame.draw.rect(win,(255,255,255),(i*80,j*80,80,80))
                       
                    else:
                        pygame.draw.rect(win,(250,200,125),(i*80,j*80,80,80))
                else:
                    if j%2==0:
                        pygame.draw.rect(win,(250,200,125),(i*80,j*80,80,80))
                    else:
                        pygame.draw.rect(win,(255,255,255),(i*80,j*80,80,80))

    def gettileindex(self,x,y):
        tempx=x//80
        tempy=y//80
        return tempx,tempy
    def Display_Players(self,PLAYER_PIECES, ENEMY_PIECES, win):
        for P1 in PLAYER_PIECES:
            if PLAYER_PIECES[P1].alive:
            
                y=(PLAYER_PIECES[P1].pos.x*80)+13
                x=(PLAYER_PIECES[P1].pos.y*80)+13
                if PLAYER_PIECES[P1].color == 'W':
                    
                    PieceImg=Whitelist[PLAYER_PIECES[P1].color+PLAYER_PIECES[P1].name.lower()]
                else:
                    PieceImg=Blacklist[PLAYER_PIECES[P1].color+PLAYER_PIECES[P1].name.lower()]
                win.blit(PieceImg,(x,y))

            
        for P2 in ENEMY_PIECES:
            if ENEMY_PIECES[P2].alive:
                q=(ENEMY_PIECES[P2].pos.x*80)+13
                p=(ENEMY_PIECES[P2].pos.y*80)+13
                if ENEMY_PIECES[P1].color == 'W':
                    PieceImg=Whitelist[ENEMY_PIECES[P2].color+ENEMY_PIECES[P2].name.lower()]
                else:
                    PieceImg=Blacklist[ENEMY_PIECES[P2].color+ENEMY_PIECES[P2].name.lower()]
                        
                win.blit(PieceImg,(p,q))

######

# Strength for pieces on the board
Points = {'Pawn': 10, 'Rook': 50, 'Bishop': 30, 'Knight': 30, 'Queen': 90, 'King': 900}
    
# Directions at which the respective piece can move
PIECES_MOVING_DIRECTION = {'Queen': (front, back, right, left, diag_right_backward, diag_right_forward, diag_left_forward, diag_left_backward),
                            'Pawn': (pawn_rules, ), 
                            'Rook': (front, back, right, left),
                            'Knight': (L_front, L_back),
                            'Bishop': (diag_right_forward, diag_right_backward, diag_left_forward, diag_left_backward),
                            'King': (one_step_front, one_step_back, one_step_right, one_step_left, one_step_diag_right_forward, one_step_diag_right_backward, one_step_diag_left_backward, one_step_diag_left_forward)}
PIECES_NAMES = ['Pawn-1',
                'Pawn-2', 
                'Pawn-3', 
                'Pawn-4',  
                'Pawn-5', 
                'Pawn-6', 
                'Pawn-7', 
                'Pawn-8',
                'Rook-1',
                'Knight-1',
                'Bishop-1',
                'Queen',
                'King',
                'Bishop-2',
                'Knight-2',
                'Rook-2'
                ]
SYMBOLS = {'BPawn': '♟', 'WPawn': '♙', 'BKnight': '♞', 'WKnight':'♘', 'BBishop':'♝', 'WBishop':'♗', 'BRook':'♜', 'WRook':'♖', 'BKing':'♚', 'WKing':'♔', 'BQueen':'♛', 'WQueen':'♕'}
BLACK = 'B' 
WHITE = 'W'
EMPTY = '.'

class Piece:                   
    def __init__(self, name, pos, color): # ✅
        """
        name: Name of the piece ('King', 'Queen', 'Bishop', 'Knight', 'Rook')
        pos: x, y where x denotes the row position and y denotes the column 
        color: 'B' or 'W' which denotes Black and White respectively
        """
        self.color = color
        self.name = name
        self.num = None
        if name != 'King' and name != 'Queen':
            self.name = name[:len(name) - 2]
            self.num = name[len(name)-1]
        self.pos = Point(pos[0], pos[1])
        self.init = False
        self.alive = True

    def actions(self, board): # ✅
        """
        Returns set of all possible actions for the piece available on the board.
        """
        if self.alive:
            directions = PIECES_MOVING_DIRECTION[self.name]
            l = []
            for direction in directions:
                if direction == pawn_rules:
                    moves_available = pawn_rules(board, self.pos, self.color, self.init)
                else:
                    moves_available = direction(board, self.pos, self.color)
                if moves_available:
                    l += moves_available
            return l

    def result(self, board, action):
        """
        Returns the board that results from making piece move on the board.
        piece: Piece class Object
        action: Point class object
        """
        new_board = deepcopy(board)
        move(new_board, deepcopy(self), action)
        return new_board

    def __repr__(self): # ✅
        """
        Representation of this class
        """
        return SYMBOLS[self.color + self.name]

    def getPiecePoints(self): # ✅
        """
        Returns strength point for the piece
            • Positive strength if color is white
            • Negative strength if color is black
        """
        return Points[self.name] if self.color == WHITE else - Points[self.name]


def game_init(player): # ✅
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    if player == WHITE:
        enemy = BLACK
    else:
        enemy = WHITE
    player_pieces = {}
    enemy_pieces = {}

    def pieces_insert(board, row, pieces, color):
        for i in range(8):
            name = pieces[i]
            obj = Piece(name, (row, i), color)
            board[row][i] = obj
            if color ==  player:
                player_pieces[pieces[i]] = obj
            else:
                enemy_pieces[pieces[i]] = obj

    # Inserting Black Pawns
    pieces_insert(board, 1, PIECES_NAMES[:8], BLACK) 
    # Inserting White Pawns
    pieces_insert(board, 6, PIECES_NAMES[:8], WHITE)
    # Inserting Black (Rooks, Bishops, Knight, Queen, King)
    pieces_insert(board, 0, PIECES_NAMES[8:], BLACK)
    # Inserting White (Rooks, Bishops, Knight, Queen, King)
    pieces_insert(board, 7, PIECES_NAMES[8:], WHITE)
    return (board, player, enemy, player_pieces, enemy_pieces)


def move(board, piece, new_pos): # ✅
    """
    Moves the piece to new position in the board, if move is valid
    piece: Piece Class Object
    new_pos: Point class Object
    """
    if new_pos not in piece.actions(board):
        return False
    x, y = piece.pos.x, piece.pos.y 
    if board[new_pos.x][new_pos.y] != EMPTY:
        kill(board, board[new_pos.x][new_pos.y])
    if board[new_pos.x][new_pos.y] == EMPTY:
        board[piece.pos.x][piece.pos.y] = EMPTY
        board[new_pos.x][new_pos.y] = piece
        piece.pos.x = new_pos.x
        piece.pos.y = new_pos.y
    piece.init = True
    if piece.pos.x == x and piece.pos.y == y:
        return False
    return True

def kill(board, piece): # ✅
    """
    Kills the piece, and frees the position in the board
    board: board attribute from Game class
    piece: Piece Class Object
    """
    # print(f"Killing {piece.name} at {piece.pos}")
    board[piece.pos.x][piece.pos.y] = EMPTY # Making the piece pos empty
    piece.alive = False
    # print("Done !")


def evaluation(board): # ✅
    """
    Returns the sum of all the strength points of the pieces in the board
    """
    val = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != EMPTY:
                val += board[i][j].getPiecePoints()
    return val


def all_available_black_moves(board): # ✅
    res = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != EMPTY and board[i][j].color == BLACK:
                all_actions = (board[i][j], board[i][j].actions(board))
                res.append(all_actions)
    return res         


def all_available_white_moves(board): # ✅
    res = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != EMPTY and board[i][j].color == WHITE:
                all_actions = (board[i][j], board[i][j].actions(board))
                res.append(all_actions)
    return res        


def terminal(board): # ✅
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != EMPTY and board[i][j].name == 'King' and board[i][j].alive:
                count += 1
    return count != 2


def winner(board): # ✅
    if terminal(board):
        for i in range(8):
            for j in range(8):
                if board[i][j] != EMPTY and board[i][j].name == 'King' and board[i][j].alive:
                        return board[i][j].color
    

def display(state): # ✅
    print("-"*30)
    for row in state:
        for ele in row:
            print(ele, end=' ')
        print()
    print("-"*30)

