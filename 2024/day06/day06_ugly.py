# "quick and dirty" original solution used for submission

import sys
import pathlib


def guard_pos(grid):
    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == "^":
                return r, c
    return 0, 0


def part1(grid):
    gr, gc = guard_pos(grid)
    dir = 0

    valid = lambda gr, gc: 0 <= gr < len(grid) and 0 <= gc < len(grid[0])

    count = set()
    while valid(gr, gc):

        if dir == 0:
            if valid(gr - 1, gc) and grid[gr-1][gc] == "#":
                dir += 1
                dir %= 4
            else:
                gr -= 1
        elif dir == 1:
            if valid(gr, gc + 1) and grid[gr][gc+1] == "#":
                dir += 1
                dir %= 4
            else:
                gc += 1
        elif dir == 2:
            if valid(gr + 1, gc) and grid[gr+1][gc] == "#":
                dir += 1
                dir %= 4
            else:
                gr += 1
        elif dir == 3:
            if valid(gr, gc - 1) and grid[gr][gc-1] == "#":
                dir += 1
                dir %= 4
            else:
                gc -= 1

        count.add((gr, gc))


    return len(count) - 1


def positions(gr, gc, grid):
    dir = 0

    valid = lambda gr, gc: 0 <= gr < len(grid) and 0 <= gc < len(grid[0])

    count = set()

    while valid(gr, gc):

        print(gr, gc)
        if dir == 0:
            if valid(gr - 1, gc) and grid[gr-1][gc] == "#":
                dir += 1
                dir %= 4
            else:
                gr -= 1
        elif dir == 1:
            if valid(gr, gc + 1) and grid[gr][gc+1] == "#":
                dir += 1
                dir %= 4
            else:
                gc += 1
        elif dir == 2:
            if valid(gr + 1, gc) and grid[gr+1][gc] == "#":
                dir += 1
                dir %= 4
            else:
                gr += 1
        elif dir == 3:
            if valid(gr, gc - 1) and grid[gr][gc-1] == "#":
                dir += 1
                dir %= 4
            else:
                gc -= 1

        count.add((gr, gc))


    return count


def loops2(gr, gc, grid):
    dir = 0

    valid = lambda gr, gc: 0 <= gr < len(grid) and 0 <= gc < len(grid[0])

    count = 0
    total = len(grid) * len(grid[0])

    while valid(gr, gc):
        if count > total:
            return True

        if dir == 0:
            if valid(gr - 1, gc) and grid[gr-1][gc] == "#":
                dir += 1
                dir %= 4
            else:
                gr -= 1
        elif dir == 1:
            if valid(gr, gc + 1) and grid[gr][gc+1] == "#":
                dir += 1
                dir %= 4
            else:
                gc += 1
        elif dir == 2:
            if valid(gr + 1, gc) and grid[gr+1][gc] == "#":
                dir += 1
                dir %= 4
            else:
                gr += 1
        elif dir == 3:
            if valid(gr, gc - 1) and grid[gr][gc-1] == "#":
                dir += 1
                dir %= 4
            else:
                gc -= 1

        count += 1

    return False


def part2(grid):
    gr, gc = guard_pos(grid)
    all_positions = positions(gr, gc, grid)
    count = 0

    for i, pos in enumerate(all_positions):
        print(i, len(all_positions), pos)
        r, c = pos

        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            grid[r][c] = "#"
            if (r, c) != (gr, gc) and loops2(gr, gc, grid):
                count += 1

            grid[r][c] = "."

    return count


def main(filename):
    with open(filename, "r") as f:
        data = f.read().strip()
        grid = [list(row) for row in data.splitlines()]

        print(f"part 1: {part1(grid)}")
        print(f"part 2: {part2(grid)}")


if __name__ == "__main__":
    basename = pathlib.Path(__file__).stem
    assert len(sys.argv) == 2, f"usage: python3 {basename} <filename>"
    main(sys.argv[1])
