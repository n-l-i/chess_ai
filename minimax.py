
from copy import copy
from helper_functions import get_parameters

class Minimax():
    def __init__(self,board):
        self.board = board
        self.colour = board.turn
        self.counter = 0
        self.moves = board.legal_moves
    
    def min_or_max(self,colour):
        if colour == self.colour:
            return max
        return min
    
    def score(self,depth):
        for i in range(1,depth+1):
            self.counter = 0
            _,scores = self.minimax_score(self.board,i,-1000,1000,self.moves)
            scores = sorted(scores,key=lambda x: x[1],reverse=True)
            self.moves = [move for move,_ in scores]
        return scores

    def minimax_score(self,board,depth,alpha,beta,moves):
        if depth == 0 or board.outcome() is not None:
            self.counter += 1
            return Minimax.evaluate(board,self.colour),[]
        scored_moves = []
        best_score = self.min_or_max(not board.turn)(1000,-1000)
        for move in moves:
            board.push(move)
            new_score,_ = self.minimax_score(board,depth-1,alpha,beta,board.legal_moves)
            board.pop()
            scored_moves.append([move,new_score])
            best_score = self.min_or_max(board.turn)(best_score,new_score)
            if board.turn == self.colour:
                alpha = max(alpha,new_score)
            else:
                beta = min(beta,new_score)
            if beta <= alpha:
                break
        return best_score,scored_moves

    def evaluate(board,colour):
        if board.outcome() is not None:
            winner = board.outcome().winner
            if winner == colour:
                return 1000
            if winner != colour:
                return -1000
            return 0
        params = get_parameters(board,colour)
        piece_value = params["friend_pieces"]-params["enemy_pieces"]
        position_value = params["friend_centre"]-params["enemy_centre"]
        return piece_value+position_value/1000
