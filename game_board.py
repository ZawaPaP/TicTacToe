class GameBoard:
    def __init__(self) -> None:
        self.board = self.initialize_board()

    def initialize_board(self) -> list:
        board = [['-' for _ in range(3)] for _ in range(3)]
        return board
