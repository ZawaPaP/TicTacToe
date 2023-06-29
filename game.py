from game_board import GameBoard
from game_status import GameStatus
from game_turn import Player


class Game:
    def __init__(self) -> None:
        self.status = GameStatus.ONGOING
        self.turn = Player.PLAYER_1
        self.winner = None
        self.board = GameBoard().board
        

    def play(self):
        if self.is_win():
            self.status = GameStatus.END
        elif self.is_draw():
            self.status = GameStatus.DRAW

    def is_win(self):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]) and self.board[i][0] != '-':
                if self.board[i][0] == Player.PLAYER_1:
                    self.winner = Player.PLAYER_1
                    self.status = GameStatus.END
                else: 
                    self.winner = Player.PLAYER_2
                    self.status = GameStatus.END
        
            pass

    def is_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    break
        self.status = GameStatus.DRAW

    def make_move(self, row, col):
        if self.board[row][col] == '-':
            player = self.turn
            self.board[row][col] = player.value
        else:
            print("Invalid move. Try again.")
        self.switch_player()

    def switch_player(self):
        if self.turn == Player.PLAYER_1:
            self.turn = Player.PLAYER_2
            print('Player 2\'s turn')
        else:
            self.turn = Player.PLAYER_1
            print('Player 1\'s turn')
