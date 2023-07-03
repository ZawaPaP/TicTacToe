from board_size import BoardSize
from board_cell import BoardCell
class GameBoard:
    def __init__(self) -> None:
        self.cell = BoardCell().initialize_cell()
        self.row = BoardSize.ROW.value
        self.col = BoardSize.COL.value

    def initialize_board(self) -> list:
        board = [[self.cell for _ in range(self.col)] for _ in range(self.row)]
        return board
