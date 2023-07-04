from game_mark import GameMark

class BoardCell:
    def __init__(self) -> None:
        self.mark = GameMark.EMPTY.value
