#!/usr/bin/env python
import re


def parse_data():
    with open("part2.txt") as f:
        data = [i.strip("\n") for i in f]
    return data


def parse_record(record):
    record = record.split(";")
    record = [i.split(",") for i in record]
    record = [n.strip() for i in record for n in i]
    record = [i.split() for i in record]
    record = [[k, int(v)] for v, k in record]
    record = [dict([i]) for i in record]
    return record


def parse_id(id_):
    result = re.search(r"\d+", id_).group()
    return int(result)


def main():
    final = []
    data = parse_data()
    data = [i.split(":") for i in data]
    data = {parse_id(k): parse_record(v) for k, v in data}
    for i in data:
        red = []
        green = []
        blue = []
        for v in data.get(i):
            match v:
                case {"red": value}:
                    red.append(value)
                case {"green": value}:
                    green.append(value)
                case {"blue": value}:
                    blue.append(value)

        final.append(max(red) * max(green) * max(blue))

    print(sum(final))


if __name__ == "__main__":
    main()
