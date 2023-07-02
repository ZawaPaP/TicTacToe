class GameBoardRenderer:
    def __init__(self, board) -> None:
        self.board = board

    def render(self) -> None:
        for row in self.board:
            print(' | '.join(row)) 
        print("\n")