from board_size import BoardSize

class GameBoardRenderer:
    def __init__(self, board) -> None:
        self.board = board
        self.row = BoardSize.ROW.value
        self.col = BoardSize.COL.value

    def render(self) -> None:
        for i in range(self.row):
            for j in range(self.col):
                if j != self.col - 1:
                    print(f" {self.board[i][j]} ", end = '|')
                else:
                    print(f" {self.board[i][j]} ")
            if i != self.row - 1:
                for k in range(self.col):
                    if k != self.col - 1:
                        print("---", end = '+')
                    else:
                        print('---')
