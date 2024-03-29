import os
import platform
from user import User
from utils import (
    YACHT_DICE_TEXT,
    DICES_DRAW,
    RED_COLOR,
    BLUE_COLOR,
    YELLOW_COLOR,
    CYAN_COLOR,
    GREEN_COLOR,
    END_COLOR,
)
import display


CLEAR = "cls" if platform.system() == "Windows" else "clear"


def print_logo():
    os.system(CLEAR)
    print(YACHT_DICE_TEXT)
    while True:
        try:
            n = int(input("플레이 할 인원 수를 입력하세요(2 ~ 4): "))
            break
        except ValueError:
            os.system(CLEAR)
            print(YACHT_DICE_TEXT)
    return n


def game_display(cnt: int, turn: int, user_lst: list, cp: int):
    os.system(CLEAR)
    dices = user_lst[cp].dices.get_dices()
    choice_number, choice_score = user_lst[cp].pick_score()
    mid = len(choice_score) // 2
    one_choice = choice_score[:mid]
    two_choice = choice_score[mid:]
    if len(user_lst) == 2:
        disp = display.two_player(turn, user_lst)
    elif len(user_lst) == 3:
        disp = display.three_player(turn, user_lst)
    else:
        disp = display.four_player(turn, user_lst)

    for i, d in enumerate(disp.split("\n")):
        if i == 8:
            d += f"      Count: {cnt} / 3"
        if 10 <= i <= 16:
            for j in range(5):
                if 10 <= i <= 12:
                    if dices[j][1] == 1:
                        d += f"      {GREEN_COLOR}{DICES_DRAW[i - 10]}{END_COLOR}"
                    else:
                        d += f"      {DICES_DRAW[i - 10]}"
                elif 13 <= i <= 15:
                    if dices[j][1] == 1:
                        d += f"      {GREEN_COLOR}{DICES_DRAW[dices[j][0] + 2][i - 13]}{END_COLOR}"
                    else:
                        d += f"      {DICES_DRAW[dices[j][0] + 2][i - 13]}"
                elif i == 16:
                    if dices[j][1] == 1:
                        d += f"      {GREEN_COLOR}{DICES_DRAW[-1]}{END_COLOR}"
                    else:
                        d += f"      {DICES_DRAW[-1]}"
        elif i == 22:
            for one_c in one_choice:
                d += "      " + one_c.ljust(20, " ")
        elif i == 23:
            for two_c in two_choice:
                d += "      " + two_c.ljust(20, " ")
        print(d)
    if cnt == 3:
        if cp == 0:
            p = RED_COLOR + "1p" + END_COLOR
        elif cp == 1:
            p = BLUE_COLOR + "2p" + END_COLOR
        elif cp == 2:
            p = YELLOW_COLOR + "3p" + END_COLOR
        else:
            p = CYAN_COLOR + "4p" + END_COLOR
        while True:
            try:
                choice = int(input(f"점수를 선택하세요({p}): "))
                if choice in choice_number:
                    return choice
            except ValueError:
                game_display(cnt, turn, user_lst, cp)


def game_result(user_lst: list) -> str:
    os.system(CLEAR)
    if len(user_lst) == 2:
        return display.two_result(user_lst)
    elif len(user_lst) == 3:
        return display.three_result(user_lst)
    else:
        return display.four_result(user_lst)


if __name__ == "__main__":
    ans, flag = "n", False
    while True:
        if flag:
            while True:
                ans = input("동일한 플레이어로 진행하시겠습니까?(y/n): ")
                if ans == "y" or ans == "n":
                    break
        if ans == "n":
            flag = False
        if not flag:
            while True:
                num = print_logo()
                if 2 <= num <= 4:
                    break

            users = []
            for idx in range(num):
                if idx == 0:
                    play = RED_COLOR + "1p" + END_COLOR
                elif idx == 1:
                    play = BLUE_COLOR + "2p" + END_COLOR
                elif idx == 2:
                    play = YELLOW_COLOR + "3p" + END_COLOR
                else:
                    play = CYAN_COLOR + "4p" + END_COLOR
                name = input(f"{play} 이름을 입력하세요: ")
                users.append(User(name))
        else:
            tmp = []
            for user in users:
                tmp.append(user.name)
            users = []
            for user in tmp:
                users.append(User(user))

        for t in range(1, 13):
            for idx, user in enumerate(users):
                c = 1
                tmp = 1
                while c < 4:
                    user.dices.random_dice()
                    tmp = 1 if tmp != 6 else 6
                    if c < 3 and tmp != 6:
                        while 0 < tmp < 6:
                            game_display(c, t, users, idx)
                            tmp = user.dices.pick_dices(c, idx)
                    else:
                        c = 3
                        user.dices.pick_dices(c, idx)
                        user.set_score(game_display(c, t, users, idx))
                    c += 1
        display.print_winner(game_result(users))
        re_game = input("게임을 다시 하려면 r을 누르세요: ")
        flag = True
        if re_game != "r":
            break
