import sys
import pathlib


def check_row(row):
    N = len(row)

    if N == 1:
        return True

    if row[0] > row[1]:
        row = row[::-1]

    for i in range(1, N):
        diff = row[i] - row[i-1]
        if (diff <= 0) or (diff > 3):
            return False

    return True


def part1(data):
    return sum(check_row(row) for row in data)


def part2(data):
    count = 0
    for row in data:
        count += any(check_row(row[:i] + row[i+1:]) for i in range(len(data)))
    return count


def main(filename):
    data = []
    with open(filename, "r") as f:
        data = f.read().strip().splitlines()

    parsed = [[int(j) for j in data[i].split()] for i in range(len(data))]

    print(f"part 1: {part1(parsed)}")
    print(f"part 2: {part2(parsed)}")


if __name__ == "__main__":
    basename = pathlib.Path(__file__).stem
    assert len(sys.argv) == 2, f"usage: python3 {basename} <filename>"
    main(sys.argv[1])
