from game_board import GameBoard
from game_status import GameStatus
from game_action import GameAction
from game_turn import Player
from io_controller import IOController
from board_renderer import GameBoardRenderer
from game_action_handler import GameActionHandler
from typing import Optional
        

class Game:
    def __init__(self) -> None:
        self.status = GameStatus.ONGOING
        self.turn = Player.PLAYER_1
        self.winner = None
        self.board = GameBoard().board
        self.controller = IOController()



    def play(self) -> Optional[GameAction]:
        print("TicTacToe Game START!\n")
        print('Player 1\'s turn\n')
        GameBoardRenderer(self.board).render()
        
        while self.status == GameStatus.ONGOING:
            input_data = self.controller.handle_input("Please input the marking position 'row, column': ")
            if 'position' in input_data:
                try:
                    self.make_move(input_data)
                    GameBoardRenderer(self.board).render()
                except ValueError as e:
                    print(str(e))
                    pass
                
            elif 'command' in input_data:
                action = GameActionHandler().game_action_handler(input_data['command'])
                if action == GameAction.EXIT or action == GameAction.RESET:
                    return action
                else:
                    continue

            if self.is_win():
                print(f"{self.turn} win")
                self.status = GameStatus.END
            elif self.is_draw():
                print("draw game")
                self.status = GameStatus.DRAW
            else:
                self.switch_player()
        return self.make_action()


    def make_move(self, input_data) -> None:
        row, col = input_data['position']
        if self.board[row - 1][col - 1] == '-':
            player = self.turn
            self.board[row - 1][col - 1] = player.value
            print(f"{player} marked in {row}, {col}")
        else:
            raise ValueError("The position is already marked. Please choose an empty position.")


    def make_action(self) -> Optional[GameAction]:
        input_data = self.controller.handle_input("E: exit the game, R: reset the game: ")
        if 'command' in input_data:
                action = GameActionHandler().game_action_handler(input_data['command'])
                if action == GameAction.EXIT or action == GameAction.RESET:
                    return action
        else:
            return self.make_action()


    def is_win(self) -> bool:
        # row
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]) and self.board[i][0] != '-':
                self.winner = self.board[i][0]
                return True
        # col
        for j in range(3):
            if (self.board[0][j] == self.board[1][j] == self.board[2][j]) and self.board[0][j] != '-':
                self.winner = self.board[0][j]
                return True
        # cross
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != '-':
            self.winner = self.board[0][0]
            return True
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] != '-':
            self.winner = self.board[0][2]
            return True
        return False


    def is_draw(self) -> bool:
        if self.is_win():
            return False
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        return True

    def switch_player(self) -> None:
        if self.turn == Player.PLAYER_1:
            self.turn = Player.PLAYER_2
            print('Player 2\'s turn\n')
        else:
            self.turn = Player.PLAYER_1
            print('Player 1\'s turn\n')
