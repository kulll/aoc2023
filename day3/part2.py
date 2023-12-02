#!/usr/bin/env python


def parse_data():
    with open("part2.txt") as f:
        data = [i.strip("\n") for i in f]
    return data


def run(data):
    """
    >>> data = "1 2 3"
    >>> run(data)
    1 2 3
    """
    print("1 2 3")


def main():
    data = parse_data()
    run(data)


if __name__ == "__main__":
    main()
