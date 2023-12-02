#!/usr/bin/env python
import re


def parse_data():
    with open("part1.txt") as f:
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
        for v in data.get(i):
            match v:
                case {"red": value} if value > 12:
                    break
                case {"green": value} if value > 13:
                    break
                case {"blue": value} if value > 14:
                    break
        else:
            final.append(i)

    print(sum(final))


if __name__ == "__main__":
    main()
