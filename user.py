from dices import Dices
from utils import CATEGORIES
from collections import Counter


class User:
    def __init__(self, name) -> None:
        self.score = ["-" for _ in range(13)]
        self.name = name
        self.dices = Dices()

    @staticmethod
    def _cal_score(i: int, dices_int: list) -> int:
        if 0 <= i < 6:
            return dices_int.count(i + 1) * (i + 1)
        elif i < 9:
            return sum(dices_int)
        elif i == 9:
            return 15
        elif i == 10:
            return 30
        elif i == 11:
            return 50
        elif i == 12:
            return 35

    @staticmethod
    def _is_straight(dice_int: list):
        for i in range(len(dice_int) - 1):
            if dice_int[i + 1] - dice_int[i] != 1:
                return 0
        return 1

    @staticmethod
    def _possible_score(self, i: int, s: str, dices_cnt: list, dices_int: list):
        if s != "-":
            return 0

        if 0 <= i <= 6:
            return 1
        elif i == 7 and dices_cnt[0][1] >= 4:
            return 1
        elif i == 8 and dices_cnt[0][1] == 3 and dices_cnt[1][1] == 2:
            return 1
        elif i == 9 and (
            self._is_straight(dices_int[:4]) or self._is_straight(dices_int[1:])
        ):
            return 1
        elif i == 10 and self._is_straight(dices_int):
            return 1
        elif i == 11 and dices_cnt[0][1] == 5:
            return 1
        return 2

    def pick_score(self):
        dices_int = [i for i, _ in self.dices.get_dices()]
        dices_cnt = Counter(dices_int).most_common()
        choice_number, choice_score = [], []
        for i, s in enumerate(self.score):
            if i == 12:
                continue
            flag = self._possible_score(self, i, s, dices_cnt, sorted(dices_int))
            if flag == 1:
                choice_score.append(
                    f"{i + 1}. {CATEGORIES[i]}: {self._cal_score(i, dices_int)}"
                )
                choice_number.append(i + 1)
            elif flag == 2:
                choice_score.append(f"{i + 1}. {CATEGORIES[i]}: 0")
                choice_number.append(i + 1)
        return choice_number, choice_score

    def set_score(self, num: int):
        dices_int = [i for i, _ in self.dices.get_dices()]
        dices_cnt = Counter(dices_int).most_common()
        flag = self._possible_score(
            self, num - 1, self.score[num - 1], dices_cnt, sorted(dices_int)
        )
        if flag == 1:
            self.score[num - 1] = str(self._cal_score(num - 1, dices_int))
        elif flag == 2:
            self.score[num - 1] = str(0)
        self.dices.reset_dice()

    def get_score(self):
        return self.score
