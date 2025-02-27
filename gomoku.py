import numpy as np

class Gomoku:
    def __init__(self, board_size=15, win_size=5):
        self.board_size = board_size
        self.win_size = win_size
        self.board = np.zeros((board_size, board_size), dtype=int)

    def list_valid_actions(self):
        return [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i, j] == 0]

    def perform_action(self, action, player):
        x, y = action
        if self.board[x, y] == 0:
            self.board[x, y] = player
            return True
        return False

    def is_winner(self, player):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.check_win(i, j, player):
                    return True
        return False

    def check_win(self, x, y, player):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 0
            for k in range(self.win_size):
                nx, ny = x + k * dx, y + k * dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.board[nx, ny] == player:
                    count += 1
                else:
                    break
            if count == self.win_size:
                return True
        return False

    def display_board(self):
        print(self.board)
