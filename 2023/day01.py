import aoc
import sys

RAW = aoc.day(1)
DATA = RAW.strip().splitlines()


def part_one() -> int:
    tot = 0
    for line in DATA:
        filtered = ''.join([n for n in line if n.isdigit()])
        tot += int(filtered[0] + filtered[-1])
    return tot


def part_two() -> int:

    d = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    tot = 0
    for line in DATA:
        nums = []
        for i in range(len(line)):
            if line[i].isdigit():
                nums.append(line[i])
                continue
            for entry in d:
                if line[i:].startswith(entry):
                    nums.append(d[entry])
        tot += int(nums[0] + nums[-1])

    return tot


if len(sys.argv) > 1 and sys.argv[1] == "--no-submit":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
else:
    aoc.submit(1, part_one)
    aoc.submit(1, part_two)
