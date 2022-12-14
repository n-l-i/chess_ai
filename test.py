from chess import Board,WHITE,BLACK,SQUARES
from random import choice
from ai import Ai
from helper_functions import get_pieces
from game import get_ai_move
from time import time
from statistics import mean

def test():
    test_speed()

def test_speed():
    tries = 5
    boards = [random_board() for _ in range(tries)]
    for depth in range(1,7):
        times = []
        print(depth,":")
        for i in range(tries):
            board = boards[i]
            ai = Ai("a")
            ai.set_colour(board.turn)
            start_time = time()
            ai_moves = ai.score_moves(board,depth)
            times.append(time()-start_time)
            print("   ",times[-1])
        times = sorted(times)
        print("   =",mean(times[1:-1]))

def see_all_moves():
    board = random_board()
    print_board(board)
    print()
    ai = Ai("a")
    ai.set_colour(board.turn)
    ai_moves = ai.score_moves(board,4)
    ai_move = get_ai_move(board)
    print_dots = [True,True]
    for i,move_score in enumerate(ai_moves):
        move,score = move_score
        if move == ai_move:
            if i in range(3):
                print_dots[0] = False
            if i in range(len(ai_moves)-3,len(ai_moves)):
                print_dots[1] = False
    for i,move_score in enumerate(ai_moves):
        move,score = move_score
        if move == ai_move:
            print(f"#{i+1}".ljust(3),move,":",score,"(selected)")
        elif i in (0,1,len(ai_moves)-2,len(ai_moves)-1):
            print(f"#{i+1}".ljust(3),move,":",score)
        if i == 1 and print_dots[0]:
            print("...")
        if i == len(ai_moves)-3 and print_dots[1]:
            print("...")

def print_board(board):
    board_str = "\n".join([f"{8-i}    {line}    {8-i}" for i,line in enumerate(str(board).split("\n"))])
    board_str = f"     A B C D E F G H\n\n{board_str}\n\n     A B C D E F G H"
    print(board_str)

def random_board():
    while True:
        board = Board()
        n_moves = choice(range(50,150))
        for _ in range(n_moves):
            if not list(board.legal_moves):
                break
            move = choice(list(board.legal_moves))
            board.push(move)
        if not list(board.legal_moves):
            continue
        white_pieces = len(get_pieces(board)[WHITE])
        black_pieces = len(get_pieces(board)[BLACK])
        min_pieces = min(white_pieces,black_pieces)
        max_pieces = max(white_pieces,black_pieces)
        if min_pieces < 3:
            continue
        if max_pieces >= min_pieces*2:
            continue
        if max_pieces >= min_pieces+6:
            continue
        break
    return board

test()
