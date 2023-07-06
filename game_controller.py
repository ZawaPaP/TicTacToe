from game import Game
from game_rule import GameRule
from io_controller import ConsoleIO
from game_mode import GameMode

class GameController:
    def start(self):
        #while True:
            mode = self.select_mode()
            game = Game(mode)
            game.play()
        #    if not self.ask_continue():
        #        break

            
    """
    def play(self, players):
        self.display_initial_text(game)
        game_rule = GameRule(game.board)
        while True:
            try:
                game.mark()
                GameBoardRenderer(game.board).render()
                if game_rule.is_over():
                    break
                game.switch_player()
                
            except ValueError or IndexError as e:
                print(f"expected error {e}")
            except Exception as e:
                print(str(e))
                exit(1)

        if game_rule.has_winner(): 
            print(f"{game.turn.name} win")
            return
        elif game_rule.is_draw():
            print("draw game")
            return
    """

    def select_mode(self) -> GameMode:
        """
        game_mode = [str(mode.name) +": "+ str(mode.value) for mode in GameMode]
        user_input = ConsoleIO.get_input(int(
            str(game_mode) + "\n Select Game mode: "
            ))
        return GameMode(int(user_input))
        """
        return GameMode(3)

    @staticmethod
    def display_initial_text(game):
        print("TicTacToe Game START!\n")
        print(f'{game.turn.name}\'s turn')
        GameBoardRenderer(game.board).render()

    def ask_continue(self) -> bool:
        if self.is_confirmed_input("continue the new game? (y/n): "):
            return True
        return False

    @staticmethod
    def is_confirmed_input(text: str) -> bool:    
        confirmation = ConsoleIO.get_input(text)
        return confirmation.lower() == "y"

