from game_mark import GameMark

class GameRule:
    def __init__(self, game) -> None:
        self.board = game.board

    def is_over(self) -> bool:
            if self.has_winner() or self.is_draw():
                return True
            return False

    def has_winner(self) -> bool:
        # row
        for i in range(self.board.row()):
            if (self.board.get_mark(i, 0) == self.board.get_mark(i, 1) == self.board.get_mark(i, 2)) and self.board.get_mark(i, 0) != GameMark.EMPTY.value:
                return True
        # col
        for j in range(self.board.column()):
            if (self.board.get_mark(0, j) == self.board.get_mark(1, j) == self.board.get_mark(2, j)) and self.board.get_mark(0, j) != GameMark.EMPTY.value:
                return True

        # cross
        if all(self.board.get_mark(i, i) == self.board.get_mark(0, 0) != GameMark.EMPTY.value for i in range(self.board.row())):
            return True
            
        if (self.board.get_mark(0, 2) == self.board.get_mark(1, 1) == self.board.get_mark(2, 0)) and self.board.get_mark(0, 2) != GameMark.EMPTY.value:
            return True
        return False

    def is_draw(self) -> bool:
        for i in range(self.board.row()):
            for j in range(self.board.column()):
                if self.board.get_mark(i, j) == GameMark.EMPTY.value:
                    return False
        return True
