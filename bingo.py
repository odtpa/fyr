import random


def s(round_num):
    unchanged = 0

    changed = 0

    options = 3

    for i in range(round_num):

        bingo_num = random.randint(0, options)

        first_choice = random.randint(0, options)

        while True:
            dropped_num = random.randint(0, options)
            if dropped_num == first_choice:
                continue
            if dropped_num == bingo_num:
                continue
            break

        while True:
            second_choice = random.randint(0, options)
            if second_choice == first_choice:
                continue
            if second_choice == dropped_num:
                continue
            break

        if bingo_num == first_choice:
            unchanged += 1
        elif bingo_num == second_choice:
            changed += 1

    print('unchanged {}%, changed{}%'.format(unchanged / round_num * 100, changed / round_num * 100))

    return unchanged, changed


if __name__ == '__main__':

    total = []

    r = 10000
    t = 100
    for i in range(t):
        print(str(i) + ':', end='')
        a, b = s(r)
        total.append((a, b))

    a_sum = 0
    b_sum = 0
    for a, b in total:
        a_sum += a
        b_sum += b
    print('average:unchanged {}%, changed{}%'.format(a_sum / (r * t) * 100, b_sum / (r * t) * 100))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
