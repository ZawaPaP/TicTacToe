from game import Game
from game_status import GameStatus


def main():
    while True:
        game = Game()
        game.play()
        if game.status == GameStatus.END:
            break

if __name__ == "__main__":
    main()
