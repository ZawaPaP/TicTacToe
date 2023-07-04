from game import Game
from board_renderer import GameBoardRenderer
from game_rule import GameRule
from console_io import ConsoleIO
from enum import Enum



class GameMode(Enum):
    PVP = 1
    VS_CPU = 2


class GameController:
    FIRST_MOVE = 'PLAYER_1'
    SECOND_MOVE = 'PLAYER_2'

    def start(self):
        while True:
            self.__play()
            if not self.ask_continue():
                break
    
    def __play(self): #play
        game_mode = self.get_game_mode()
        game = Game()
        self.display_initial_text(game)
        while True:
            #try:
                game.mark()
                GameBoardRenderer(game.board).render()
                if GameRule(game).is_over():
                    break
                game.switch_player()
            # 想定するエラーだけ別定義して、処理を別にする
            # Exception > str(e) > exit(1)
            #except 
            
            #except Exception as e:
            #    print(str(e))
            #    exit(1)        
        if GameRule(game).has_winner(): 
            print(f"{game.turn.value} win")
            return
        elif GameRule(game).is_draw():
            print("draw game")
            return

    def get_game_mode(self) -> str:
        game_mode = [str(mode.name) +": "+ str(mode.value) for mode in GameMode]
        return ConsoleIO.get_input(
            str(game_mode) + "\n Select Game mode: "
            )

    def set_game_mode(self, mode: int) -> GameMode:
        return GameMode(mode)
        
    @staticmethod
    def display_initial_text(game):
        print("TicTacToe Game START!\n")
        print(f'{game.turn.value}\'s turn\n')
        GameBoardRenderer(game.board).render()


    def ask_continue(self) -> bool:
        if self.is_confirmed_input("continue the new game? (y/n): "):
            return True
        return False

    @staticmethod
    def is_confirmed_input(text: str) -> bool:    
        confirmation = ConsoleIO.get_input(text)
        return confirmation.lower() == "y"
