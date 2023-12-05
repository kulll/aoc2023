#!/usr/bin/env python
from string import digits, punctuation

import numpy as np


def parse_data():
    with open("part1.txt") as f:
        data = [i.strip("\n") for i in f]
    return data


def check_symbols(data, symbols_coordinate):
    touched = []
    x, y = symbols_coordinate
    north = x, y + 1
    south = x, y - 1
    west = x - 1, y
    east = x + 1, y
    north_east = x + 1, y + 1
    south_east = x + 1, y - 1
    north_west = x - 1, y + 1
    south_west = x - 1, y - 1
    for point in (
        north,
        south,
        west,
        east,
        north_east,
        south_east,
        north_west,
        south_west,
    ):
        touched_num = np.char.isdigit(data[point])
        touched_num = np.compress(touched_num, point, axis=1)
        touched_num = np.stack(touched_num, axis=1)
        touched.append(touched_num)
    touched = [i for i in touched if i.size]
    touched = np.array([n for i in touched for n in i])
    return touched


def parse_numbers(data):
    temp = []
    final = []

    for i, v in np.ndenumerate(data):
        if v in digits:
            temp.append((v, i))
        else:
            if not temp:
                continue
            num = "".join([num for num, index in temp])
            index = [index for num, index in temp]
            final.append((num, index))
            temp.clear()

    return final


def check_touched(number, symbols):
    final = []
    for num, index in number:
        for i in index:
            if x := (symbols == i).all(axis=1).nonzero():
                [x] = x
                if x.size:
                    final.append(int(num))
                    break
    return final


def run(data):
    """
    >>> data = [
    ... "467..114..",
    ... "...*......",
    ... "..35..633.",
    ... "......#...",
    ... "617*......",
    ... ".....+.58.",
    ... "..592.....",
    ... "......755.",
    ... "...$.*....",
    ... ".664.598..",
    ... ]
    >>> run(data)
    4361
    """
    data = [[n for n in i] for i in data]
    data = np.array(data)
    target = punctuation.replace(".", "")
    target = list(target)
    symbols_coordinate = np.where(np.isin(data, target))
    symbols_result = check_symbols(data, symbols_coordinate)
    number_result = parse_numbers(data)
    final = check_touched(number_result, symbols_result)
    print(sum(final))


def main():
    data = parse_data()
    run(data)


if __name__ == "__main__":
    main()
