import os
import platform
from user import User
from utils import (
    YACHT_DICE_TEXT,
    CATEGORIES,
    DICES_DRAW,
    GREEN_COLOR,
    BLUE_COLOR,
    RED_COLOR,
    END_COLOR,
)


CLEAR = "cls" if platform.system() == "Windows" else "clear"


def print_logo():
    os.system(CLEAR)
    print(YACHT_DICE_TEXT)
    input()


def score_board():
    print("|", end=" ")
    print("{:^10}".format("name"), end=" ")
    for c in CATEGORIES:
        print(f"| {c:^11} ", end="")
    print("|")


def game_display(cnt: int, turn: int, op: User, tp: User, cp: int):
    os.system(CLEAR)
    op_sc, tp_sc = op.get_score(), tp.get_score()
    op_subtotal, tp_subtotal = 0, 0
    op_total, tp_total = 0, 0
    for i, (one, two) in enumerate(zip(op_sc, tp_sc)):
        if one.isdigit():
            op_total += int(one)
            if i < 6:
                op_subtotal += int(one)
        if two.isdigit():
            tp_total += int(two)
            if i < 6:
                tp_subtotal += int(two)
    if op_subtotal > 62 and op_sc[-1] == "-":
        op_sc[-1] = "35"
        op.set_score(13)
    if tp_subtotal > 62 and tp_sc[-1] == "-":
        tp_sc[-1] = "35"
        tp.set_score(13)
    dices = op.dices.get_dices() if cp == 0 else tp.dices.get_dices()
    choice_number, choice_score = op.pick_score() if cp == 0 else tp.pick_score()
    mid = len(choice_score) // 2
    one_choice = choice_score[:mid]
    two_choice = choice_score[mid:]
    display = f"""
    ---------------------------
    | Turn {str(turn).rjust(2, " ")}/12  |           |
    |-------------------------|
    | Categories  |  1p |  2p |
    |-------------------------|
    | Aces        | {RED_COLOR}{str(op_sc[0]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[0]).rjust(3, " ")}{END_COLOR} |
    | Deuces      | {RED_COLOR}{str(op_sc[1]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[1]).rjust(3, " ")}{END_COLOR} |
    | Threes      | {RED_COLOR}{str(op_sc[2]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[2]).rjust(3, " ")}{END_COLOR} |
    | Fours       | {RED_COLOR}{str(op_sc[3]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[3]).rjust(3, " ")}{END_COLOR} |
    | Fives       | {RED_COLOR}{str(op_sc[4]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[4]).rjust(3, " ")}{END_COLOR} |
    | Sixes       | {RED_COLOR}{str(op_sc[5]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[5]).rjust(3, " ")}{END_COLOR} |
    |-------------------------|
    |  Subtotal   | {RED_COLOR}{str(op_subtotal).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_subtotal).rjust(3, " ")}{END_COLOR} |
    |  Bonus(+35) | {RED_COLOR}{str(op_sc[12]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[12]).rjust(3, " ")}{END_COLOR} |
    |-------------------------|
    | Choice      | {RED_COLOR}{str(op_sc[6]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[6]).rjust(3, " ")}{END_COLOR} |
    | 4 of a Kind | {RED_COLOR}{str(op_sc[7]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[7]).rjust(3, " ")}{END_COLOR} |
    | Full House  | {RED_COLOR}{str(op_sc[8]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[8]).rjust(3, " ")}{END_COLOR} |
    | S. Straight | {RED_COLOR}{str(op_sc[9]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[9]).rjust(3, " ")}{END_COLOR} |
    | L. Straight | {RED_COLOR}{str(op_sc[10]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[10]).rjust(3, " ")}{END_COLOR} |
    | Yacht       | {RED_COLOR}{str(op_sc[11]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[11]).rjust(3, " ")}{END_COLOR} |
    |-------------------------|
    |    Total    | {RED_COLOR}{str(op_total).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_total).rjust(3, " ")}{END_COLOR} |
    ---------------------------
    """

    for i, d in enumerate(display.split("\n")):
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
        p = "1p" if cp == 0 else "2p"
        while True:
            try:
                choice = int(input(f"Choice the Score({p}): "))
                if choice in choice_number:
                    return choice
            except ValueError:
                continue


def game_result(op: User, tp: User):
    os.system(CLEAR)
    op_sc, tp_sc = op.get_score(), tp.get_score()
    op_total, tp_total = 0, 0
    op_subtotal, tp_subtotal = 0, 0
    for i, (one, two) in enumerate(zip(op_sc, tp_sc)):
        if one.isdigit():
            op_total += int(one)
            if i < 6:
                op_subtotal += int(one)
        if two.isdigit():
            tp_total += int(two)
            if i < 6:
                tp_subtotal += int(two)
    if op_sc[-1] == "-":
        op_sc[-1] = "0"
    if tp_sc[-1] == "-":
        tp_sc[-1] = "0"
    display = f"""
        ---------------------------
        | Turn 12/12  |           |
        |-------------------------|
        | Categories  |  1p |  2p |
        |-------------------------|
        | Aces        | {RED_COLOR}{str(op_sc[0]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[0]).rjust(3, " ")}{END_COLOR} |
        | Deuces      | {RED_COLOR}{str(op_sc[1]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[1]).rjust(3, " ")}{END_COLOR} |
        | Threes      | {RED_COLOR}{str(op_sc[2]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[2]).rjust(3, " ")}{END_COLOR} |
        | Fours       | {RED_COLOR}{str(op_sc[3]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[3]).rjust(3, " ")}{END_COLOR} |
        | Fives       | {RED_COLOR}{str(op_sc[4]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[4]).rjust(3, " ")}{END_COLOR} |
        | Sixes       | {RED_COLOR}{str(op_sc[5]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[5]).rjust(3, " ")}{END_COLOR} |
        |-------------------------|
        |  Subtotal   | {RED_COLOR}{str(op_subtotal).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_subtotal).rjust(3, " ")}{END_COLOR} |
        |  Bonus(+35) | {RED_COLOR}{str(op_sc[12]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[12]).rjust(3, " ")}{END_COLOR} |
        |-------------------------|
        | Choice      | {RED_COLOR}{str(op_sc[6]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[6]).rjust(3, " ")}{END_COLOR} |
        | 4 of a Kind | {RED_COLOR}{str(op_sc[7]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[7]).rjust(3, " ")}{END_COLOR} |
        | Full House  | {RED_COLOR}{str(op_sc[8]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[8]).rjust(3, " ")}{END_COLOR} |
        | S. Straight | {RED_COLOR}{str(op_sc[9]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[9]).rjust(3, " ")}{END_COLOR} |
        | L. Straight | {RED_COLOR}{str(op_sc[10]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[10]).rjust(3, " ")}{END_COLOR} |
        | Yacht       | {RED_COLOR}{str(op_sc[11]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[11]).rjust(3, " ")}{END_COLOR} |
        |-------------------------|
        |    Total    | {RED_COLOR}{str(op_total).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_total).rjust(3, " ")}{END_COLOR} |
        ---------------------------
        """
    print(display)


if __name__ == "__main__":
    print_logo()
    one_p, two_p = User("one_p"), User("two_p")
    users = [one_p, two_p]

    for t in range(1, 13):
        for idx, user in enumerate(users):
            c = 1
            tmp = 1
            while c < 4:
                user.dices.random_dice()
                tmp = 1 if tmp != 6 else 6
                if c < 3 and tmp != 6:
                    while 0 < tmp < 6:
                        game_display(c, t, one_p, two_p, idx)
                        tmp = user.dices.pick_dices(c, idx)
                else:
                    c = 3
                    user.dices.pick_dices(c, idx)
                    user.set_score(game_display(c, t, one_p, two_p, idx))
                c += 1
    print(game_result(one_p, two_p))
