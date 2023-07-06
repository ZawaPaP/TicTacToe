import random

class CPUStrategy:
    @staticmethod
    def generate_low_level_cpu_move(board) -> int:
        while True:
            row = random.randint(1, 3)
            column = random.randint(1, 3)
            if board.is_empty(row, column):
                return row, column

    def generate_high_level_cpu_move(self) -> int:
        #自分がリーチの場合、勝つ
        #相手がリーチか確認し、防ぐ
        #中心が空いていたら取得 
        #空いていない場合、角が空いていれば角をランダム取得
        #空いている場所をランダム取得

        pass