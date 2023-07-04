class GameBoardRenderer:
    def __init__(self, board) -> None:
        self.board = board

    def render(self) -> None:
        for i in range(1, self.board.row() + 1):
            for j in range(1, self.board.column() + 1):
                if j != self.board.column():
                    print(f" {self.board.get_mark(i, j)} ", end = '|')
                else:
                    print(f" {self.board.get_mark(i, j)} ")
            if i != self.board.row():
                for k in range(1, self.board.column() + 1):
                    if k != self.board.column():
                        print("---", end = '+')
                    else:
                        print('---')
        print("\n")
