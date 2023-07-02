from game import Game
from game_action import GameAction

def main():
    game = Game()
    action = game.play()
    if action == GameAction.EXIT:
        print("Exit the game")
        return
    elif action == GameAction.RESET:
        print("Reset the game")
        main()
    else:
        print("Unexpected action. Exit the game")
        return

if __name__ == "__main__":
    main()
