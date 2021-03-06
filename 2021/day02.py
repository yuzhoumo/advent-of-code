import aoc
import sys

RAW = aoc.day(2)
DATA = [(d, int(a)) for d, a in re.findall("(\w+) (\d+)", RAW)]

def part_one() -> int:
    """
    Computes final x, y position given an array of
    directions to travel and distances. "up", "down" moves vertically
    while "forward" moves horizontally. Return x * y.
    """
    x = y = 0
    for direction, amt in DATA:
        match direction:
            case "up":
                y -= amt
            case "down":
                y += amt
            case "forward":
                x += amt

    return x * y


def part_two() -> int:
    """
    Computes final x, y position given that "up", "down"
    commands adjust "aim" and "forward" command moves x forward
    n units and aim * amt units deeper. Return x * y.
    """
    x = y = aim = 0
    for direction, amt in DATA:
        match direction:
            case "up":
                aim -= amt
            case "down":
                aim += amt
            case "forward":
                x += amt
                y += aim * amt

    return x * y


if len(sys.argv) > 1 and sys.argv[1] == "--no-submit":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
else:
    aoc.submit(2, part_one)
    aoc.submit(2, part_two)
