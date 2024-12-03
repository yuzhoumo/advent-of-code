import sys
import pathlib
import re


def multiply(s):
    nums = s[:-1][4:].split(",")
    return int(nums[0]) * int(nums[1])


def part1(data):
    pattern = re.compile(r"mul\(\d+,\d+\)")
    matches = re.findall(pattern, data)

    res = 0
    for m in matches:
        res += multiply(m)

    return res


def part2(data):
    pattern = re.compile(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))")
    matches = re.findall(pattern, data)
    res = 0
    should_mul = True
    for m in matches:
        mul, do, dont = m

        if do:
            should_mul = True

        if dont:
            should_mul = False

        if mul and should_mul:
            res += multiply(mul)

    return res


def main(filename):
    with open(filename, "r") as f:
        data = f.read().strip()

        print(f"part 1: {part1(data)}")
        print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    basename = pathlib.Path(__file__).stem
    assert len(sys.argv) == 2, f"usage: python3 {basename} <filename>"
    main(sys.argv[1])
