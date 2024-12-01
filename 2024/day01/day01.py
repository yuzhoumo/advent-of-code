import sys
import pathlib


def part1(l1, l2):
    pairs = zip(sorted(l1), sorted(l2))
    return sum(abs(n1 - n2) for n1, n2 in pairs)


def part2(l1, l2):
    counts = {}
    for n in l2:
        counts[n] = counts.get(n, 0) + 1
    return sum(n * counts.get(n, 0) for n in l1)


def main(filename):
    rows = []
    with open(filename, "r") as f:
        rows = f.read().strip().splitlines()

    list1, list2 = [], []
    for row in rows:
        n1, n2 = row.split()
        list1.append(int(n1))
        list2.append(int(n2))

    print(f"part 1: {part1(list1, list2)}")
    print(f"part 2: {part2(list1, list2)}")


if __name__ == "__main__":
    basename = pathlib.Path(__file__).stem
    assert len(sys.argv) == 2, f"usage: python3 {basename} <filename>"
    main(sys.argv[1])

