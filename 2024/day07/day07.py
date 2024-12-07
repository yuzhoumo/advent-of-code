import sys
import pathlib


def calibrate(equations, ops):
    def can_solve(nums, test, curr, i):
        if i >= len(nums):
            return curr == test

        for op in ops:
            if can_solve(nums, test, op(curr, nums[i]), i + 1):
                return True

    tot = 0
    for test, nums in equations:
        if can_solve(nums, test, nums[0], 1):
            tot += test

    return tot


def part1(equations):
    ops = [int.__add__, int.__mul__]
    return calibrate(equations, ops)


def part2(equations):
    ops = [int.__add__, int.__mul__, lambda a, b: int(str(a) + str(b))]
    return calibrate(equations, ops)


def main(filename):
    with open(filename, "r") as f:
        data = f.read().strip()
        equations = []
        for line in data.splitlines():
            key, rest = line.split(":")
            equations.append([int(key), [int(n) for n in rest.split()]])

        print(f"part 1: {part1(equations)}")
        print(f"part 2: {part2(equations)}")


if __name__ == "__main__":
    basename = pathlib.Path(__file__).stem
    assert len(sys.argv) == 2, f"usage: python3 {basename} <filename>"
    main(sys.argv[1])
