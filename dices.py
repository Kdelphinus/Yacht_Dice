import random, utils


class Dices:
    def __init__(self):
        self.dices = [[0, 0] for _ in range(5)]

    def random_dice(self):
        for i in range(5):
            if self.dices[i][1] == 0:
                self.dices[i][0] = random.randint(1, 6)

    def reset_dice(self):
        self.dices = [[0, 0] for _ in range(5)]

    def get_dices(self):
        return self.dices

    def pick_dices(self, cnt: int, idx: int) -> int:
        p = "1p" if idx == 0 else "2p"
        if cnt == 3:
            for i in range(5):
                self.dices[i][1] = 1
            return 6
        while True:
            try:
                tmp = int(input(f"Choice the Dices({p}): "))
                if tmp == 0:
                    return 0
                if 0 < tmp < 6:
                    self.dices[tmp - 1][1] = 0 if self.dices[tmp - 1][1] == 1 else 1
                    return tmp
                elif tmp == 6:
                    for i in range(5):
                        self.dices[i][1] = 1
                    return 6
            except ValueError:
                continue
