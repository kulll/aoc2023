#!/usr/bin/env python
from argparse import ArgumentParser
from string import digits
from collections import deque


def get_first_digit(data):
    return data.popleft()


def get_last_digit(data):
    return data.pop()


def filter_digit(data):
    filtered = []
    for n in data:
        filtered.append([i for i in n if i in digits])
    return filtered


def parse_data():
    with open("part1.txt") as f:
        data = [i.strip("\n") for i in f]
    return data


def main():
    total = []
    data = parse_data()
    data = filter_digit(data)

    for i in data:
        first = get_first_digit(deque(i))
        second = get_last_digit(deque(i))
        combined = int(first + second)
        total.append(combined)

    result = sum(total)
    print(result)


if __name__ == "__main__":
    main()
