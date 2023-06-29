from game import Game

class TextRenderer:
    def __init__(self, game) -> None:
        self.game = game

    def win_render(self, player):
        print(f"{player} win the game!")

    def draw_render(self):
        print("draw game")

    def continue_render(self):
        print("draw game")
