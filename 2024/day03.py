import aoc
import re


def multiply(s):
    nums = s[:-1][4:].split(",")
    return int(nums[0]) * int(nums[1])


def part1(data):
    pattern = re.compile(r"mul\(\d+,\d+\)")
    matches = re.findall(pattern, data)
    return sum(multiply(m) for m in matches)


def part2(data):
    pattern = re.compile(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))")
    matches = re.findall(pattern, data)

    res, should_mul = 0, True
    for m in matches:
        mul, do, dont = m

        if do:
            should_mul = True

        if dont:
            should_mul = False

        if mul and should_mul:
            res += multiply(mul)

    return res


def main(text, part=None):
    data = text.strip()

    if part is None or part == 1:
        print(f"part 1: {part1(data)}")
    if part is None or part == 2:
        print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    aoc.run(main, 3)
