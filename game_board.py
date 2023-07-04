from board_cell import BoardCell
from game_mark import GameMark
class GameBoard:
    ROW = 3
    COLUMN = 3

    def __init__(self) -> None:
        self.board = [[BoardCell() for _ in range(self.column())] for _ in range(self.row())]
    
    def get_mark(self, row, column) -> GameMark:
        try:
            return self.board[row - 1][column - 1].mark
        except IndexError as e:
            print(str(e))

    def set_mark(self, row, column, mark) -> None:
        try:
            self.board[row - 1][column - 1].mark = mark
        except IndexError as e:
            print(f"{e} out of range with set_mark")
            exit(1)

    def row(self) -> int:
        return GameBoard.ROW

    def column(self) -> int:
        return GameBoard.COLUMN
