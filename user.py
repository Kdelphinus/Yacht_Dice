from dices import Dices

CATEGORIES = ["Aces", "Deuces", "Threes", "Fours", "Fives", "Sixes", "Choice", "4 of a Kind", "Full House", "Small Straight", "Large Straight", "Yacht"]


class User:
    def __init__(self, name):
        self.score = [0] * 12
        self.name = name
        self.dices = Dices()
    
    @staticmethod
    def _cal_score(i: int, dices: list) -> int:
        if 0 <= i < 6:
            return dices.count(i + 1) * (i + 1)
        elif i < 9:
            return sum(dices)
        elif i == 9:
            return 15
        elif i == 10:
            return 30
        elif i == 11:
            return 50
    
    def roll_dice(self):
        self.dices.roll_dices()
        self.dices.print_dices()
        self.dices.pick_dices()
            
    def pick_score(self):
        for i, s in enumerate(self.score):
            if s == 0:
                print(f"{i}. {CATEGORIES[i]}")
        
        n = int(input("점수를 선택해주세요."))
        while n < 0 or 12 < n or self.score[n] != 0:
            n = int(input("잘못된 번호를 입력했습니다. 다시 입력하세요."))
        self.score[n] = self._cal_score(n, self.dices.get_dices())
    
    def get_score(self):
        print("|", end=" ")
        print(f"{self.name:^20}", end=" ")
        for s in self.score:
            print(f"| {s:^2} ", end="")
        print(" |")
