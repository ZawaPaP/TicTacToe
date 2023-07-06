from typing import List
from board import GameBoard
from board_renderer import GameBoardRenderer
from player_manager import PlayerManager
from game_mode import GameMode
from game_rule import GameRule
from player_type import PlayerType
from io_controller import IOController
from cpu_logic import CPUStrategy

class Game:
    def __init__(self, game_mode) -> None:
        self.players = PlayerManager().get_players(self.set_player_type(game_mode))
        self.turn = self.players[0]
        self.board = GameBoard()

    def play(self):
        while True:
            try:
                self.mark()
                GameBoardRenderer(self.board).render()
                if GameRule.is_over(self.board):
                    break
                self.switch_player()
                
            except ValueError or IndexError as e:
                print(f"expected error {e}")
            #except Exception as e:
            #    print(str(e))
            #    exit(1)

        if GameRule.has_winner(self.board): 
            print(f"{self.turn.name} win")
            return
        elif GameRule.is_draw(self.board):
            print("draw game")
            return

    def mark(self) -> None:
        if PlayerManager.is_cpu():
            row, column = self.get_cpu_move()
        else:
            row, column = self.get_user_move()
        try:
            self.make_move(row, column)
        except Exception:
            raise Exception

    def make_move(self, row, column) -> None:
        if self.board.is_empty(row, column):
            self.board.set_mark(row, column, self.turn.mark)
            print(f"{self.turn.name} marked in {row}, {column}\n")
        else:
            raise ValueError("The position is already marked. Please choose an empty cell.")

    def get_user_move(self) -> int:
        return IOController.handle_input("Mark 'row, column': ")

    def get_cpu_move(self) -> int:
        return CPUStrategy.generate_low_level_cpu_move(self.board)

    def switch_player(self):
        if self.turn == self.players[0]:
            self.turn = self.players[1]
        else:
            self.turn = self.players[0]
        print(f'{self.turn.name}\'s turn')

    def set_player_type(self, game_mode) -> List[PlayerType]:
        if game_mode == GameMode.CVC:
            player_types = [
                PlayerType.CPU,
                PlayerType.CPU
            ]
        elif game_mode == GameMode.PVC:
            player_types = [
                PlayerType.USER, 
                PlayerType.CPU
                ]
            if self.choice_first_player == 2:
                player_types.reverse()
            
        else:
            player_types = [
                PlayerType.USER,
                PlayerType.USER
            ]
        return player_types

    @staticmethod
    def choice_first_player() -> int:
        while True:
            choice = IOController.get_integer_input(
                """
                Choose 1 for being the first player / Choose 2 for letting the CPU take the first turn.
                Please enter your choice: 
                """
            )
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter either 1 or 2.")
