from game_mark import GameMark

class BoardCell:
    def __init__(self) -> None:
        self.mark = GameMark.EMPTY.value

class GameBoard:
    ROW = 3
    COLUMN = 3

    def __init__(self) -> None:
        self.board = [[BoardCell() for _ in range(self.column())] for _ in range(self.row())]

    def get_mark(self, row, column) -> GameMark:
        try:
            return self.board[row - 1][column - 1].mark
        except IndexError:
            raise IndexError

    def set_mark(self, row, column, mark) -> None:
        try:
            self.board[row - 1][column - 1].mark = mark
        except IndexError:
            raise IndexError

    def is_empty(self, row, column) -> bool:
        return self.board[row - 1][column - 1].mark == GameMark.EMPTY.value

    def is_reach(self, mark) -> bool:
        pass

    def empty_corner(self) -> int:
        pass

    @staticmethod
    def row() -> int:
        return GameBoard.ROW

    @staticmethod
    def column() -> int:
        return GameBoard.COLUMN

    def row_range(self) -> range:
        return range(1, self.row() + 1)

    def column_range(self) -> range:
        return range(1, self.column() + 1)

    def get_center_position(self) -> int:
        return (self.row() + 1) // 2, (self.column() + 1) // 2

    def get_row_mark(self, i) -> list:
        return [mark for mark in [self.board[i - 1][j - 1].mark for j in self.column_range()]]
