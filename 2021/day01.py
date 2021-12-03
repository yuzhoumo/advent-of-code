import aoc
import sys

RAW = aoc.day(1)
DATA = [int(n) for n in RAW.splitlines()]

def num_increasing(nums):
    """
    Returns the number of times the ith number in a sequence is
    greater than the number before it.
    """
    return sum(nums[i] > nums[i-1] for i in range(1, len(nums)))


def part_one() -> int:
    return num_increasing(DATA)


def part_two() -> int:
    """
    Returns the number of times the ith sliding window sum of 3
    numbers in a sequence is greater than the sum before it.
    """
    sums = [sum(DATA[i:i+3]) for i in range(len(DATA) - 2)]
    return num_increasing(sums)


if len(sys.argv) > 1 and sys.argv[1] == "--no-submit":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
else:
    aoc.submit(1, part_one)
    aoc.submit(1, part_two)
    