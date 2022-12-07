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
        if idx == 0:
            p = utils.RED_COLOR + "1p" + utils.END_COLOR
        elif idx == 1:
            p = utils.BLUE_COLOR + "2p" + utils.END_COLOR
        elif idx == 2:
            p = utils.YELLOW_COLOR + "3p" + utils.END_COLOR
        else:
            p = utils.CYAN_COLOR + "4p" + utils.END_COLOR
        if cnt == 3:
            for i in range(5):
                self.dices[i][1] = 1
            return 6
        while True:
            try:
                print("- 주사위 킵하기: 1 ~ 5")
                print("- 다시 주사위 던지기: 0")
                print("- 바로 점수 계산하기: 6")
                tmp = int(input(f"주사위를 선택하세요({p}): "))
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
