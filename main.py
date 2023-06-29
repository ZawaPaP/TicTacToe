from board_renderer import GameBoardRenderer
from game import Game

def main():
    game = Game()
    renderer = GameBoardRenderer(game)
    renderer.render() 
    game.make_move(1, 1)
    renderer.render()

if __name__ == "__main__":
    main()
