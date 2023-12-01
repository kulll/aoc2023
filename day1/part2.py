#!/usr/bin/env python
from argparse import ArgumentParser
from collections import deque

DIGITS = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_digit(data):
    result = [data.find(d) for d in DIGITS.keys()]
    result = [i for i in result if i >= 0]
    result = min(result)
    for d in DIGITS.keys():
        if data.find(d) == result:
            return DIGITS.get(d)


def get_last_digit(data):
    result = [data.rfind(d) for d in DIGITS.keys()]
    result = [i for i in result if i >= 0]
    result = max(result)
    for d in DIGITS.keys():
        if data.rfind(d) == result:
            return DIGITS.get(d)


def parse_data():
    with open("part2.txt") as f:
        data = [i.strip("\n") for i in f]
    return data


def main():
    total = []
    data = parse_data()

    for i in data:
        first = get_first_digit(i)
        second = get_last_digit(i)
        combined = int(first + second)
        total.append(combined)
        print(f"{combined}", i)

    result = sum(total)
    print(result)


if __name__ == "__main__":
    main()
