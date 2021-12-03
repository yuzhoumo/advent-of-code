import aoc
import sys
from collections import Counter

RAW = aoc.day(3)
DATA = [i for i in RAW.split()]

def common_bit(position, data, lcb_mode=False):
    counts = Counter([x[position] for x in data])
    if lcb_mode: return int(counts['1'] < counts['0'])
    return int(counts['1'] >= counts['0'])


def part_one():
    gamma = epsilon = ''
    for i in range(len(DATA[0])):
        mcb = common_bit(i, DATA)
        epsilon += str(mcb ^ 1)
        gamma += str(mcb)

    return int(gamma, 2) * int(epsilon, 2)


def part_two():
    def get_rating(lcb_mode=False):
        buf, i = DATA, 0
        while len(buf) != 1 and i < len(DATA[0]):
            bit_criteria = common_bit(i, buf, lcb_mode)
            buf = [x for x in buf if x[i] == str(bit_criteria)]
            i += 1

        return int(buf[0], 2)

    return get_rating() * get_rating(lcb_mode=True)


if len(sys.argv) > 1 and sys.argv[1] == "--no-submit":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
else:
    aoc.submit(3, part_one)
    aoc.submit(3, part_two)
