import os, random

DICES_DRAW = (
    "  +------+",
    " /      /|",
    "+-----+  |",
    ("|     |  |", "|  @  |  |", "|     | / "),
    ("|@    |  |", "|     |  |", "|    @| / "),
    ("|@    |  |", "|  @  |  |", "|    @| / "),
    ("|@   @|  |", "|     |  |", "|@   @| / "),
    ("|@   @|  |", "|  @  |  |", "|@   @| / "),
    ("|@   @|  |", "|@   @|  |", "|@   @| / "),
    "+-----+   ",
)
BLUE_COLOR = ("\033[96m", "\033[0m")

class Dices:
    def __init__(self):
        self.dices = [[0, 0] for _ in range(5)]
        
    def roll_dices(self):
        for i in range(5):
            if self.dices[i][1] == 0:
                self.dices[i][0] = random.randint(1, 6)
            
    def reset_dice(self):
        self.dices = [[0, 0]] * 5
    
    def get_dices(self):
        return self.dices
    
    def print_dices(self):
        for i in range(7):
            for j in range(5):
                if i < 3:
                    if self.dices[j][1] == 1:
                        print(f"{BLUE_COLOR[0]}{DICES_DRAW[i]}{BLUE_COLOR[1]}", end="")
                    else:
                        print(f"{DICES_DRAW[i]}", end="")
                elif i < 6:
                    if self.dices[j][1] == 1:
                        print(f"{BLUE_COLOR[0]}{DICES_DRAW[self.dices[j][0] + 2][i - 3]}{BLUE_COLOR[1]}", end="")
                    else:
                        print(f"{DICES_DRAW[self.dices[j][0] + 2][i - 3]}", end="")
                else:
                    if self.dices[j][1] == 1:
                        print(f"{BLUE_COLOR[0]}{DICES_DRAW[-1]}{BLUE_COLOR[1]}", end="")
                    else:
                        print(f"{DICES_DRAW[-1]}", end="")
            print()
    
    def pick_dices(self):
        print("선택할 주사위의 번호(1 ~ 5)를 입력하세요. 입력이 끝나면 0을 눌러주세요.")
        while True:
            try:
                tmp = int(input())
                if tmp == 0:
                    break
                if 0 < tmp < 6:
                    self.dices[tmp - 1][1] = 0 if self.dices[tmp - 1][1] == 1 else 1
                    self.print_dices()
                else:
                    print("잘못된 번호입니다. 다시 입력하세요.")
            except ValueError:
                print("잘못된 입력입니다. 1 ~ 5 사이의 숫자를 입력하세요.")

dices = Dices()
dices.roll_dices()
print(dices.get_dices())
dices.print_dices()
dices.pick_dices()