import chess
from ai import Ai
from random import choice,uniform

def push_move(board,move,):
    move = chess.Move.from_uci(move)
    if move not in board.legal_moves:
        raise ValueError(f"{move} is not a legal move.")
    board.push(move)
    return board

def get_ai_move(board,thinking_time):
    ai = Ai("ai")
    ai.set_colour(board.turn)
    thinking_time = thinking_time*(choice(range(75,150))/100)
    scored_moves = ai.score_moves(board,thinking_time)
    ai_move = choose_move(scored_moves)
    return ai_move

def choose_move(scored_moves):
    scored_moves = sorted(scored_moves,key=lambda x: x[1],reverse=True)
    # Always choose the best move
    return scored_moves[0][0]
