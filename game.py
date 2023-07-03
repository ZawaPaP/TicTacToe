from game_board import GameBoard
from game_status import GameStatus
from game_command import GameCommand
from game_turn import Player
from io_controller import IOController
from board_renderer import GameBoardRenderer
from game_command_handler import GameCommandHandler
from game_rule import GameRule
from game_mark import GameMark
        

class Game:
    def __init__(self) -> None:
        self.status = GameStatus.ONGOING
        self.turn = Player.PLAYER_1
        self.winner = None
        self.board = GameBoard().initialize_board()
        self.controller = IOController()
        self.rule = GameRule(self.board)

    def play(self) -> str:
        print("TicTacToe Game START!\n")
        print('Player 1\'s turn\n')
        GameBoardRenderer(self.board).render()
        
        while self.status == GameStatus.ONGOING:
            input_data = self.controller.handle_input("Input the marking position 'row, column': ")
            if 'position' in input_data:
                try:
                    self.make_move(input_data)
                    GameBoardRenderer(self.board).render()
                except ValueError as e:
                    print(str(e))
                    continue
            elif 'command' in input_data:
                self.make_action(input_data)

            if self.rule.has_winner():
                print(f"{self.turn} win")
                self.status = GameStatus.END
            elif self.rule.is_draw():
                print("draw game")
                self.status = GameStatus.END
            else:
                self.switch_player()


    def make_move(self, input_data) -> None:
        row, col = input_data['position']
        if self.board[row - 1][col - 1] == GameMark.EMPTY.value:
            player = self.turn
            self.board[row - 1][col - 1] = player.value
            print(f"{player} marked in {row}, {col}")
        else:
            raise ValueError("The position is already marked. Please choose an empty position.")

    def make_action(self, input_data) -> None:
        GameCommandHandler().game_command_handler(input_data['command'])

    def switch_player(self):
        if self.turn == Player.PLAYER_1:
            self.turn = Player.PLAYER_2
            print('Player 2\'s turn\n')
        else:
            self.turn = Player.PLAYER_1
            print('Player 1\'s turn\n')
