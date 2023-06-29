from game import Game

class GameBoardRenderer:
    def __init__(self, game) -> None:
        self.board = game.board

    def render(self):
        for row in self.board:
            print(' | '.join(row)) 
