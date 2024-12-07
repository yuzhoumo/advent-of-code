import aoc


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


def main(text):
    data = text.strip().splitlines()
    parsed = [[int(j) for j in data[i].split()] for i in range(len(data))]
    return part1(parsed), part2(parsed)


if __name__ == "__main__":
    aoc.run(main, 2)
