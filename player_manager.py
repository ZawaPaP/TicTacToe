from player import Player
from player_type import PlayerType
from game_mark import GameMark
from typing import List

class PlayerManager:
    def __init__(self) -> None:
        self.cpu_counter = 0
        self.game_marks = GameMark.get_game_marks()
    
    def get_players(self, player_types: List[PlayerType]) -> List[Player]:
        players = []
        for i in range(len(player_types)):
            player = self.create_player(player_types[i])
            player = self.assign_mark(i, player)
            players.append(player)
        return players

    def create_player(self, type: PlayerType) -> Player:
        if type == PlayerType.CPU:
            return self.create_cpu_player()
        else:
            return self.create_user_player()

    def create_cpu_player(self) -> Player:
        self.cpu_counter += 1
        cpu_name = f"CPU_{self.cpu_counter}"
        return Player(cpu_name, PlayerType.CPU)

    def create_user_player(self, user_name) -> Player:
        return Player(user_name, PlayerType.USER)

    def assign_mark(self, index, player: Player) -> Player:
        try:
            player.mark = self.game_marks[index]
            return player
        except IndexError:
            print("Not enough game marks.")
            exit(1)

    @staticmethod
    def get_player_type(player: Player):
        try:
            return player.type
        except IndexError:
            raise IndexError("there is no player type")
    
    @staticmethod
    def is_cpu(player: Player) -> bool:
        return PlayerManager.get_player_type(player) == PlayerType.CPU

    @staticmethod
    def is_user(player: Player) -> bool:
        return PlayerManager.get_player_type(player) == PlayerType.USER
