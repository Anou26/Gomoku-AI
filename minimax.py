import numpy as np

class MinimaxAI:
    def __init__(self, depth=3):
        self.depth = depth

    def minimax(self, board, depth, is_maximizing):
        valid_moves = board.list_valid_actions()
        if depth == 0 or board.is_winner(1) or board.is_winner(-1):
            return self.evaluate(board)

        if is_maximizing:
            best_score = float('-inf')
            for move in valid_moves:
                board.perform_action(move, 1)
                score = self.minimax(board, depth - 1, False)
                board.perform_action(move, 0)  # Undo move
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for move in valid_moves:
                board.perform_action(move, -1)
                score = self.minimax(board, depth - 1, True)
                board.perform_action(move, 0)
                best_score = min(best_score, score)
            return best_score

    def evaluate(self, board):
        return np.random.randint(-10, 10)  # Placeholder heuristic

    def best_move(self, board):
        best_score = float('-inf')
        best_action = None
        for move in board.list_valid_actions():
            board.perform_action(move, 1)
            score = self.minimax(board, self.depth - 1, False)
            board.perform_action(move, 0)
            if score > best_score:
                best_score = score
                best_action = move
        return best_action
