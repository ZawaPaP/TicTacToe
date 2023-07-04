from game_board import GameBoard
from io_controller import IOController
from enum import Enum
        
class GameMark(Enum):
    EMPTY = ' '
    PLAYER_1 = 'o'
    PLAYER_2 = 'x'

'''
class Turn(Enum):
    TOP = 'PLAYER_1'
    BOTTOM = 'PLAYER_2'

class GameMode(Enum):
    PVP = 1
    PVC = 2
'''

class Game:
    def __init__(self) -> None:
        self.board = GameBoard()
        self.controller = IOController()

    def mark(self) -> str:
        try:
            input_data = self.controller.handle_input("Input the marking position 'row, column': ")
            if 'position' in input_data:
                self.make_move(input_data)
        except IndexError or ValueError as e:
            print(f"{str(e)} invalid input")

    def make_move(self, input_data) -> None:
        row, col = input_data['position']
        if self.board.get_mark(row,col) == GameMark.EMPTY.value:
            player = self.turn.value
            self.board.set_mark(row, col, GameMark[player].value)
            print(f"{player} marked in {row}, {col}\n")
        else:
            raise ValueError("The position is already marked. Please choose an empty position.")
    '''
    def make_action(self, input_data) -> None:
        GameCommandHandler().game_command_handler(input_data['command'])
    '''
    
    def switch_player(self):
        if self.turn == Turn.TOP:
            self.turn = Turn.BOTTOM
            print('Player 2\'s turn\n')
        else:
            self.turn = Turn.TOP
            print('Player 1\'s turn\n')
