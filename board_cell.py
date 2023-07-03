
from game_mark import GameMark

class BoardCell:
    def __init__(self) -> None:
        self.cell = GameMark.EMPTY.value
    
    def initialize_cell(self) -> str:
        return self.cell
