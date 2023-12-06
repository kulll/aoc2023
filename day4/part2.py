#!/usr/bin/env python
from collections import deque


def parse_data():
    with open("part1.txt") as f:
        data = [i.strip("\n") for i in f]
    return data


def mutate_kuato(card, count, offset):
    return list(range((card + offset), card + count + offset))


def run(data):
    """
    >>> data = [
    ... "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    ... "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    ... "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    ... "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    ... "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    ... "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ... ]
    >>> run(data)
    30
    """
    initial_round = []
    final = []
    data = [i.split(":") for i in data]
    for i, v in data:
        offset = 1
        _, card = i.split()
        card = int(card)
        winning, mine = v.split("|")
        winning, mine = winning.split(), mine.split()
        win = [i for i in mine if i in winning]
        count = len(win)
        mutated = mutate_kuato(card, count, offset)
        initial_round.append(mutated)
        final.append(card)


    second_round = deque(i for i in initial_round)
    while second_round:
        value = second_round.pop()

        if not value:
            continue

        for i in value:
            final.append(i)
            if result := mutate_kuato(i, len(initial_round[i - 1]), 1):
                second_round.appendleft(result)

    print(len(final))

def main():
    data = parse_data()
    run(data)


if __name__ == "__main__":
    main()
