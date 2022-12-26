from user import User
from utils import (
    GREEN_COLOR,
    BLUE_COLOR,
    RED_COLOR,
    YELLOW_COLOR,
    CYAN_COLOR,
    END_COLOR,
)


def two_player(turn: int, users: list):
    op_sc, tp_sc = users[0].get_score(), users[1].get_score()
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
        users[0].set_score(13)
    if tp_subtotal > 62 and tp_sc[-1] == "-":
        tp_sc[-1] = "35"
        users[1].set_score(13)
    display = f"""
    ---------------------------
    | Turn {str(turn).rjust(2, " ")}/12  |           |
    |-------------------------|
    | Categories  |  {RED_COLOR}1p{END_COLOR} |  {BLUE_COLOR}2p{END_COLOR} |
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
    return display


def two_result(users: list):
    op_sc, tp_sc = users[0].get_score(), users[1].get_score()
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
            | Categories  |  {RED_COLOR}1p{END_COLOR} |  {BLUE_COLOR}2p{END_COLOR} |
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
    if op_total > tp_total:
        return RED_COLOR + users[0].name + END_COLOR
    elif op_total < tp_total:
        return BLUE_COLOR + users[1].name + END_COLOR
    else:
        return GREEN_COLOR + "draw" + END_COLOR


def three_player(turn: int, users: list):
    op_sc, tp_sc, th_sc = (
        users[0].get_score(),
        users[1].get_score(),
        users[2].get_score(),
    )
    op_subtotal, tp_subtotal, th_subtotal = 0, 0, 0
    op_total, tp_total, th_total = 0, 0, 0
    for i, (one, two, three) in enumerate(zip(op_sc, tp_sc, th_sc)):
        if one.isdigit():
            op_total += int(one)
            if i < 6:
                op_subtotal += int(one)
        if two.isdigit():
            tp_total += int(two)
            if i < 6:
                tp_subtotal += int(two)
        if three.isdigit():
            th_total += int(three)
            if i < 6:
                th_subtotal += int(three)
    if op_subtotal > 62 and op_sc[-1] == "-":
        op_sc[-1] = "35"
        users[0].set_score(13)
    if tp_subtotal > 62 and tp_sc[-1] == "-":
        tp_sc[-1] = "35"
        users[1].set_score(13)
    if th_subtotal > 62 and th_sc[-1] == "-":
        th_sc[-1] = "35"
        users[2].set_score(13)
    display = f"""
        ---------------------------------
        | Turn {str(turn).rjust(2, " ")}/12  |                 |
        |-------------------------------|
        | Categories  |  {RED_COLOR}1p{END_COLOR} |  {BLUE_COLOR}2p{END_COLOR} |  {YELLOW_COLOR}3p{END_COLOR} |
        |-------------------------------|
        | Aces        | {RED_COLOR}{str(op_sc[0]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[0]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[0]).rjust(3, " ")}{END_COLOR} |
        | Deuces      | {RED_COLOR}{str(op_sc[1]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[1]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[1]).rjust(3, " ")}{END_COLOR} |
        | Threes      | {RED_COLOR}{str(op_sc[2]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[2]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[2]).rjust(3, " ")}{END_COLOR} |
        | Fours       | {RED_COLOR}{str(op_sc[3]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[3]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[3]).rjust(3, " ")}{END_COLOR} |
        | Fives       | {RED_COLOR}{str(op_sc[4]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[4]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[4]).rjust(3, " ")}{END_COLOR} |
        | Sixes       | {RED_COLOR}{str(op_sc[5]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[5]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[5]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------|
        |  Subtotal   | {RED_COLOR}{str(op_subtotal).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_subtotal).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_subtotal).rjust(3, " ")}{END_COLOR} |
        |  Bonus(+35) | {RED_COLOR}{str(op_sc[12]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[12]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[12]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------|
        | Choice      | {RED_COLOR}{str(op_sc[6]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[6]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[6]).rjust(3, " ")}{END_COLOR} |
        | 4 of a Kind | {RED_COLOR}{str(op_sc[7]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[7]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[7]).rjust(3, " ")}{END_COLOR} |
        | Full House  | {RED_COLOR}{str(op_sc[8]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[8]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[8]).rjust(3, " ")}{END_COLOR} |
        | S. Straight | {RED_COLOR}{str(op_sc[9]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[9]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[9]).rjust(3, " ")}{END_COLOR} |
        | L. Straight | {RED_COLOR}{str(op_sc[10]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[10]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[10]).rjust(3, " ")}{END_COLOR} |
        | Yacht       | {RED_COLOR}{str(op_sc[11]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[11]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[11]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------|
        |    Total    | {RED_COLOR}{str(op_total).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_total).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_total).rjust(3, " ")}{END_COLOR} |
        ---------------------------------
        """
    return display


def three_result(users: list):
    op_sc, tp_sc, th_sc = (
        users[0].get_score(),
        users[1].get_score(),
        users[2].get_score(),
    )
    op_subtotal, tp_subtotal, th_subtotal = 0, 0, 0
    op_total, tp_total, th_total = 0, 0, 0
    for i, (one, two, three) in enumerate(zip(op_sc, tp_sc, th_sc)):
        if one.isdigit():
            op_total += int(one)
            if i < 6:
                op_subtotal += int(one)
        if two.isdigit():
            tp_total += int(two)
            if i < 6:
                tp_subtotal += int(two)
        if three.isdigit():
            th_total += int(three)
            if i < 6:
                th_subtotal += int(three)
    if op_sc[-1] == "-":
        op_sc[-1] = "0"
    if tp_sc[-1] == "-":
        tp_sc[-1] = "0"
    if th_sc[-1] == "-":
        th_sc[-1] = "0"
    display = f"""
        ---------------------------------
        | Turn 12/12  |                 |
        |-------------------------------|
        | Categories  |  {RED_COLOR}1p{END_COLOR} |  {BLUE_COLOR}2p{END_COLOR} |  {YELLOW_COLOR}3p{END_COLOR} |
        |-------------------------------|
        | Aces        | {RED_COLOR}{str(op_sc[0]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[0]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[0]).rjust(3, " ")}{END_COLOR} |
        | Deuces      | {RED_COLOR}{str(op_sc[1]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[1]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[1]).rjust(3, " ")}{END_COLOR} |
        | Threes      | {RED_COLOR}{str(op_sc[2]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[2]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[2]).rjust(3, " ")}{END_COLOR} |
        | Fours       | {RED_COLOR}{str(op_sc[3]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[3]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[3]).rjust(3, " ")}{END_COLOR} |
        | Fives       | {RED_COLOR}{str(op_sc[4]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[4]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[4]).rjust(3, " ")}{END_COLOR} |
        | Sixes       | {RED_COLOR}{str(op_sc[5]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[5]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[5]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------|
        |  Subtotal   | {RED_COLOR}{str(op_subtotal).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_subtotal).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_subtotal).rjust(3, " ")}{END_COLOR} |
        |  Bonus(+35) | {RED_COLOR}{str(op_sc[12]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[12]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[12]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------|
        | Choice      | {RED_COLOR}{str(op_sc[6]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[6]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[6]).rjust(3, " ")}{END_COLOR} |
        | 4 of a Kind | {RED_COLOR}{str(op_sc[7]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[7]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[7]).rjust(3, " ")}{END_COLOR} |
        | Full House  | {RED_COLOR}{str(op_sc[8]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[8]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[8]).rjust(3, " ")}{END_COLOR} |
        | S. Straight | {RED_COLOR}{str(op_sc[9]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[9]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[9]).rjust(3, " ")}{END_COLOR} |
        | L. Straight | {RED_COLOR}{str(op_sc[10]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[10]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[10]).rjust(3, " ")}{END_COLOR} |
        | Yacht       | {RED_COLOR}{str(op_sc[11]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[11]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[11]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------|
        |    Total    | {RED_COLOR}{str(op_total).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_total).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_total).rjust(3, " ")}{END_COLOR} |
        ---------------------------------
            """
    print(display)
    if op_total > tp_total and op_total > th_total:
        return RED_COLOR + users[0].name + END_COLOR
    elif tp_total > op_total and tp_total > th_total:
        return BLUE_COLOR + users[1].name + END_COLOR
    elif th_total > op_total and th_total > tp_total:
        return YELLOW_COLOR + users[2].name + END_COLOR
    else:
        return GREEN_COLOR + "draw" + END_COLOR


def four_player(turn: int, users: list):
    op_sc, tp_sc, th_sc, fo_sc = (
        users[0].get_score(),
        users[1].get_score(),
        users[2].get_score(),
        users[3].get_score(),
    )
    op_subtotal, tp_subtotal, th_subtotal, fo_subtotal = 0, 0, 0, 0
    op_total, tp_total, th_total, fo_total = 0, 0, 0, 0
    for i, (one, two, three, four) in enumerate(zip(op_sc, tp_sc, th_sc, fo_sc)):
        if one.isdigit():
            op_total += int(one)
            if i < 6:
                op_subtotal += int(one)
        if two.isdigit():
            tp_total += int(two)
            if i < 6:
                tp_subtotal += int(two)
        if three.isdigit():
            th_total += int(three)
            if i < 6:
                th_subtotal += int(three)
        if four.isdigit():
            fo_total += int(four)
            if i < 6:
                fo_subtotal += int(four)
    if op_subtotal > 62 and op_sc[-1] == "-":
        op_sc[-1] = "35"
        users[0].set_score(13)
    if tp_subtotal > 62 and tp_sc[-1] == "-":
        tp_sc[-1] = "35"
        users[1].set_score(13)
    if th_subtotal > 62 and th_sc[-1] == "-":
        th_sc[-1] = "35"
        users[2].set_score(13)
    if fo_subtotal > 62 and fo_sc[-1] == "-":
        fo_sc[-1] = "35"
        users[3].set_score(13)
    display = f"""
        ---------------------------------------
        | Turn {str(turn).rjust(2, " ")}/12  |                       |
        |-------------------------------------|
        | Categories  |  {RED_COLOR}1p{END_COLOR} |  {BLUE_COLOR}2p{END_COLOR} |  {YELLOW_COLOR}3p{END_COLOR} |  {CYAN_COLOR}4p{END_COLOR} |
        |-------------------------------------|
        | Aces        | {RED_COLOR}{str(op_sc[0]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[0]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[0]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[0]).rjust(3, " ")}{END_COLOR} |
        | Deuces      | {RED_COLOR}{str(op_sc[1]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[1]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[1]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[1]).rjust(3, " ")}{END_COLOR} |
        | Threes      | {RED_COLOR}{str(op_sc[2]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[2]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[2]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[2]).rjust(3, " ")}{END_COLOR} |
        | Fours       | {RED_COLOR}{str(op_sc[3]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[3]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[3]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[3]).rjust(3, " ")}{END_COLOR} |
        | Fives       | {RED_COLOR}{str(op_sc[4]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[4]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[4]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[4]).rjust(3, " ")}{END_COLOR} |
        | Sixes       | {RED_COLOR}{str(op_sc[5]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[5]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[5]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[5]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------------|
        |  Subtotal   | {RED_COLOR}{str(op_subtotal).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_subtotal).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_subtotal).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_subtotal).rjust(3, " ")}{END_COLOR} |
        |  Bonus(+35) | {RED_COLOR}{str(op_sc[12]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[12]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[12]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[12]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------------|
        | Choice      | {RED_COLOR}{str(op_sc[6]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[6]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[6]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[6]).rjust(3, " ")}{END_COLOR} |
        | 4 of a Kind | {RED_COLOR}{str(op_sc[7]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[7]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[7]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[7]).rjust(3, " ")}{END_COLOR} |
        | Full House  | {RED_COLOR}{str(op_sc[8]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[8]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[8]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[8]).rjust(3, " ")}{END_COLOR} |
        | S. Straight | {RED_COLOR}{str(op_sc[9]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[9]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[9]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[9]).rjust(3, " ")}{END_COLOR} |
        | L. Straight | {RED_COLOR}{str(op_sc[10]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[10]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[10]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[10]).rjust(3, " ")}{END_COLOR} |
        | Yacht       | {RED_COLOR}{str(op_sc[11]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[11]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[11]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[11]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------------|
        |    Total    | {RED_COLOR}{str(op_total).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_total).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_total).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_total).rjust(3, " ")}{END_COLOR} |
        ---------------------------------------
        """
    return display


def four_result(users: list):
    op_sc, tp_sc, th_sc, fo_sc = (
        users[0].get_score(),
        users[1].get_score(),
        users[2].get_score(),
        users[3].get_score(),
    )
    op_subtotal, tp_subtotal, th_subtotal, fo_subtotal = 0, 0, 0, 0
    op_total, tp_total, th_total, fo_total = 0, 0, 0, 0
    for i, (one, two, three, four) in enumerate(zip(op_sc, tp_sc, th_sc, fo_sc)):
        if one.isdigit():
            op_total += int(one)
            if i < 6:
                op_subtotal += int(one)
        if two.isdigit():
            tp_total += int(two)
            if i < 6:
                tp_subtotal += int(two)
        if three.isdigit():
            th_total += int(three)
            if i < 6:
                th_subtotal += int(three)
        if four.isdigit():
            fo_total += int(four)
            if i < 6:
                fo_subtotal += int(four)
    if op_sc[-1] == "-":
        op_sc[-1] = "0"
    if tp_sc[-1] == "-":
        tp_sc[-1] = "0"
    if th_sc[-1] == "-":
        th_sc[-1] = "0"
    if fo_sc[-1] == "-":
        fo_sc[-1] = "0"
    display = f"""
        ---------------------------------------
        | Turn 12/12  |                       |
        |-------------------------------------|
        | Categories  |  {RED_COLOR}1p{END_COLOR} |  {BLUE_COLOR}2p{END_COLOR} |  {YELLOW_COLOR}3p{END_COLOR} |  {CYAN_COLOR}4p{END_COLOR} |
        |-------------------------------------|
        | Aces        | {RED_COLOR}{str(op_sc[0]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[0]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[0]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[0]).rjust(3, " ")}{END_COLOR} |
        | Deuces      | {RED_COLOR}{str(op_sc[1]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[1]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[1]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[1]).rjust(3, " ")}{END_COLOR} |
        | Threes      | {RED_COLOR}{str(op_sc[2]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[2]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[2]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[2]).rjust(3, " ")}{END_COLOR} |
        | Fours       | {RED_COLOR}{str(op_sc[3]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[3]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[3]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[3]).rjust(3, " ")}{END_COLOR} |
        | Fives       | {RED_COLOR}{str(op_sc[4]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[4]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[4]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[4]).rjust(3, " ")}{END_COLOR} |
        | Sixes       | {RED_COLOR}{str(op_sc[5]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[5]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[5]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[5]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------------|
        |  Subtotal   | {RED_COLOR}{str(op_subtotal).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_subtotal).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_subtotal).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_subtotal).rjust(3, " ")}{END_COLOR} |
        |  Bonus(+35) | {RED_COLOR}{str(op_sc[12]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[12]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[12]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[12]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------------|
        | Choice      | {RED_COLOR}{str(op_sc[6]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[6]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[6]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[6]).rjust(3, " ")}{END_COLOR} |
        | 4 of a Kind | {RED_COLOR}{str(op_sc[7]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[7]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[7]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[7]).rjust(3, " ")}{END_COLOR} |
        | Full House  | {RED_COLOR}{str(op_sc[8]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[8]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[8]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[8]).rjust(3, " ")}{END_COLOR} |
        | S. Straight | {RED_COLOR}{str(op_sc[9]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[9]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[9]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[9]).rjust(3, " ")}{END_COLOR} |
        | L. Straight | {RED_COLOR}{str(op_sc[10]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[10]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[10]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[10]).rjust(3, " ")}{END_COLOR} |
        | Yacht       | {RED_COLOR}{str(op_sc[11]).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_sc[11]).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_sc[11]).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_sc[11]).rjust(3, " ")}{END_COLOR} |
        |-------------------------------------|
        |    Total    | {RED_COLOR}{str(op_total).rjust(3, " ")}{END_COLOR} | {BLUE_COLOR}{str(tp_total).rjust(3, " ")}{END_COLOR} | {YELLOW_COLOR}{str(th_total).rjust(3, " ")}{END_COLOR} | {CYAN_COLOR}{str(fo_total).rjust(3, " ")}{END_COLOR} |
        ---------------------------------------
        """
    print(display)
    if op_total > tp_total and op_total > th_total and op_total > fo_total:
        return RED_COLOR + users[0].name + END_COLOR
    elif tp_total > op_total and tp_total > th_total and tp_total > fo_total:
        return BLUE_COLOR + users[1].name + END_COLOR
    elif th_total > op_total and th_total > tp_total and th_total > fo_total:
        return YELLOW_COLOR + users[2].name + END_COLOR
    elif fo_total > op_total and fo_total > tp_total and fo_total > th_total:
        return CYAN_COLOR + users[3].name + END_COLOR
    else:
        return GREEN_COLOR + "draw" + END_COLOR


def print_winner(winner: str):
    """아이디어 생기면 구현할 예정"""
    print(f"Winner: {winner}")
