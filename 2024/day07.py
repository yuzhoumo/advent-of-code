import aoc


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


def main(text):
    data = text.strip()
    equations = []
    for line in data.splitlines():
        key, rest = line.split(":")
        equations.append([int(key), [int(n) for n in rest.split()]])
    return part1(equations), part2(equations)


if __name__ == "__main__":
    aoc.run(main, 7)
