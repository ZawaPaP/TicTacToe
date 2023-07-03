from game_mark import GameMark
from board_size import BoardSize

class GameRule:
    def __init__(self, board) -> None:
        self.board = board
        self.row = BoardSize.ROW.value
        self.col = BoardSize.COL.value
    
    def is_over(self) -> bool:
        if self.has_winner or self.is_draw:
            return True 
        return False

    def has_winner(self) -> bool:
        # row
        for i in range(self.row):
            if all(cell == self.board[i][0] != GameMark.EMPTY.value for cell in self.board[i]):
                self.winner = self.board[i][0]
                return True
        # col
        for j in range(self.col):
            if (self.board[0][j] == self.board[1][j] == self.board[2][j]) and self.board[0][j] != GameMark.EMPTY.value:
                self.winner = self.board[0][j]
                return True
        # cross
        if all(self.board[i][i] == self.board[0][0] != GameMark.EMPTY.value for i in range(self.row)):
            self.winner = self.board[0][0]
            return True
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] != GameMark.EMPTY.value:
            self.winner = self.board[0][2]
            return True
        return False

    def is_draw(self) -> bool:
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == GameMark.EMPTY.value:
                    return False
        return True
