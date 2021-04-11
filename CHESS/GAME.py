import pygame
from BOARD import *
import math
###############
pygame.init()

win=pygame.display.set_mode((840,640))

pygame.display.set_caption("CHESS")

win.fill((255,255,255))

def Text(st,x,y,bg=(0,0,0),size=64,color=(255,255,255)):
    font = pygame.font.Font('SEASRN__.ttf', size) 
      
    text = font.render(st, True, color, bg) 
      
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
      
    # set the center of the rectangular object. 
    textRect.center = (x,y)
    win.blit(text,textRect)
#################
def minimize(board, depth, alpha, beta):
    if terminal(board) or depth == 0:
        return None, None, evaluation(board)
    minim = math.inf
    best_move = None
    best_choice =  None
    for actions in all_available_black_moves(board):
        piece = actions[0]
        for mv in actions[1]:
            (_, _, value) = maximize(piece.result(board, mv), depth - 1, alpha, beta)
            beta = min(beta, value)
            if value < minim:
                best_move = mv
                best_choice = piece
                minim = value
            if alpha >= beta:
                break
    #print("****OPP INFO --  ",best_choice, best_move, minim,depth,alpha,beta,"--  OPP INFO*****")        
    return best_choice, best_move, minim


def maximize(board, depth, alpha, beta):
    if terminal(board) or depth == 0:
        return None, None, evaluation(board)
    maxim = -math.inf
    best_move = None
    best_choice =  None
    for actions in all_available_white_moves(board):
        piece = actions[0]
        for mv in actions[1]:
            (_, _, value) = minimize(piece.result(board, mv), depth - 1, alpha, beta)
            alpha = max(alpha, value)
            if value > maxim:
                best_move = mv
                best_choice = piece
                maxim = value
            if alpha >= beta:
                break
    return best_choice, best_move, maxim
  

def ischeckmate_Player(board,king_pos):
    king_x=king_pos.x
    king_y=king_pos.y
    for actions in all_available_black_moves(board):
        for action in actions[1]:
            if king_x==action.x and king_y==action.y:
                
                return True
    return False
def ischeckmate_Enemy(board,king_pos):
    king_x=king_pos.x
    king_y=king_pos.y
    for actions in all_available_white_moves(board):
        #print(actions)
        for action in actions[1]:
            if king_x==action.x and king_y==action.y:
                
                return True
    return False


def get_king_pos(board,color):
    for i in range(8):
        for j in range(8):
            if board[i][j] != ".":
                if board[i][j].name=="King" and board[i][j].color == color:
                    #print(board[i][j].pos)
                    return board[i][j].pos

    
def check_win_P(board):
    for actions in all_available_black_moves(board):
        piece=actions[0]
        for action in actions[1]:
            tempboard = piece.result(board,action)
            kp = get_king_pos(tempboard,"B")
            if not ischeckmate_Enemy(tempboard,kp):
                #print(piece,action)
                return False
    return True        
def check_win_E(board):
    for actions in all_available_white_moves(board):
        piece=actions[0]
        for action in actions[1]:
            tempboard = piece.result(board,action)
            kp = get_king_pos(tempboard,"W")
            if not ischeckmate_Player(tempboard,kp):
                return False
    return True        

def edit_moves(PieceMoves,choice,BOARD):
    movelist=[]
    for m in PieceMoves:                 
        tempboard=choice.result(BOARD,m)
        kp=get_king_pos(tempboard,"W")
        if not ischeckmate_Player(tempboard,kp):
            movelist.append(m)

    return movelist

            
def main():
    Board=BOARDCLASS(win)
    PieceMoves=[]
    HighlightP=(-1,-1)
    PieceStatus=False
    isP_check=False
    isE_check=False
    run=True 
    #print("Enter your choice:\n 'B' for Black \n 'W' for White")
    #player = input("> ")
    #if player == 'B' or player == 'W':
    #    break
    player='W'
    BOARD, PLAYER, ENEMY, PLAYER_PIECES, ENEMY_PIECES = game_init(player)
    #print('Initializing Game !')
    #display(BOARD)

    n = 0 if PLAYER == 'W' else 1
    while n < 100 and run:
        win.fill((0,0,0))
        Board.draw(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN and n % 2 == 0 and PieceStatus:
                mx,my=pygame.mouse.get_pos()
                cx,cy=Board.gettileindex(mx,my)
                if move(BOARD, choice, Point(cy, cx)):
                    Board.Display_Players(PLAYER_PIECES, ENEMY_PIECES, win)
                    pygame.display.update()
                    PieceStatus=False
                    PieceMoves=[]
                    HightlightP=(-1,-1)
                    n+=1
                    pass
                else:
                    PieceStatus=False
                    HightlightP=(-1,-1)
                    PI=BOARD[cy][cx]
                    try:
                        if PI.color == 'W':
                            try:
                                piece=PI.name+'-'+PI.num
                            except:
                                piece=piece=PI.name
                            #PI=player+PI.name
                            HighlightP=(cx,cy)
                            PieceStatus=True
                            choice=PLAYER_PIECES[piece]
                            PieceMoves=choice.actions(BOARD)
                    except:
                        pass
                    
                isE_check=ischeckmate_Enemy(BOARD,ENEMY_PIECES['King'].pos)
                if isE_check:
                    if check_win_P(BOARD):
                        print("You Won")
                        run=False
                    
                
            elif event.type == pygame.MOUSEBUTTONDOWN and n % 2 == 0:
                mx,my=pygame.mouse.get_pos()
                cx,cy=Board.gettileindex(mx,my)
                
                try:
                    PI=BOARD[cy][cx]
             
                    if PI.color == 'W':
                        try:
                            piece=PI.name+'-'+PI.num
                        except:
                            piece=piece=PI.name
                        #PI=player+PI.name
                        HighlightP=(cx,cy)
                        PieceStatus=True
                        choice=PLAYER_PIECES[piece]
                        PieceMoves=choice.actions(BOARD)
                        print(isP_check)
                                 
                                    
                except:
                    pass

        Board.Display_Players(PLAYER_PIECES, ENEMY_PIECES, win)            
        if n % 2 == 0:
            #print(f"Your Turn! ({PLAYER})")
            #while True:
                #piece = input("Enter the piece name you wanna move:")
                #if piece in PLAYER_PIECES:
                    #if not PLAYER_PIECES[piece].actions(BOARD):
                        #print("Moves are not available for this piece")
                    #else:
                        #break
                #else:
                    #print("Invalid name!")
                #print("Available Pieces are:")
                #for key, obj in PLAYER_PIECES.items():
                    #if obj.alive:
                        #print(f"{key} at {obj.pos}")
            #choice = PLAYER_PIECES[piece] 
            #while True:
                #print(f"Available moves for {choice.name}: {choice.actions(BOARD)}")
                #x, y = map(int, input("Enter your move:").split())
                #if move(BOARD, choice, Point(x, y)):
                    #break
                #print("Invalid move!")
            #display(BOARD)
            try:
                PieceMoves = edit_moves(PieceMoves,choice,BOARD)
            except:
                pass
            if PieceMoves:
                for i in PieceMoves:
                    tempy=(i.x*80)+40
                    tempx=(i.y*80)+40
                    pygame.draw.circle(win,(0,255,0),(tempx,tempy),5)
            if HighlightP!=(-1,-1):
                
                pygame.draw.rect(win,(0,255,0,0.3),(HighlightP[0]*80,HighlightP[1]*80,80,80),2)
                
            Text('your turn',740,70,size=18,color=(0,255,0))
            if isP_check:
                Text('Check',740,100,size=18,color=(255,0,0))
            #print(f"Evaluation:{evaluation(BOARD)}")
            #win_check = winner(BOARD)
            #if win_check:
                #print(f"{win_check} won!")
                #break   
            
        else:
            Text('opponent turn',740,70,size=18,color=(255,0,0))
            if isE_check:
                Text('Check',740,100,size=18,color=(0,255,0))
            pygame.display.update()
            #print(f"Computer's Turn ! ({ENEMY})")
            if ENEMY == BLACK:
                #print('ai start')
                pc, mv, _ = minimize(BOARD, 3, -math.inf, math.inf)
                move(BOARD, pc, mv)
                #print('ai done')
            elif ENEMY == WHITE:
                pc, mv, _ = maximize(BOARD, 3, -math.inf, math.inf)
                move(BOARD, pc, mv)
            #display(BOARD)
            #print(f"Evaluation:{evaluation(BOARD)}")
            #win_check = winner(BOARD)
            #if win_check:
                #print(f"{win_check} won!")
                #break
            
            n+=1
            isP_check=ischeckmate_Player(BOARD,PLAYER_PIECES['King'].pos)
            if isP_check:
                    if check_win_E(BOARD):
                        print("Enemy won")
                        run=False
                
        pygame.display.update()    
    pygame.quit()
if __name__ == "__main__":
    main()
    print("GAME OVER")
