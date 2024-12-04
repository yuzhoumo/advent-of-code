import sys
import pathlib


def check(grid, r, c, word):
    n = len(word)
    count = 0

    # horizontal
    if c + n <= len(grid[0]):
        s = ''.join(grid[r][c:c+4])
        count += s == word

    # vertical
    if r + n <= len(grid):
        s = ''.join(grid[r+i][c] for i in range(n))
        count += s == word

    # diagonal down
    if (c + n <= len(grid[0])) and (r + n <= len(grid)):
        s = ''.join(grid[r+i][c+i] for i in range(n))
        count += s == word

    # diagonal up
    if (c + n <= len(grid[0])) and (r - n + 1 >= 0):
        s = ''.join(grid[r-i][c+i] for i in range(n))
        count += s == word

    return count


def check2(grid, r, c):
    if c + 1 >= len(grid[0]) or r + 1 >= len(grid) or r - 1 < 0 or c - 1 < 0:
        return 0

    s1 = ''.join(grid[r-1+i][c-1+i] for i in range(3))
    s2 = ''.join(grid[r+1-i][c-1+i] for i in range(3))

    return (s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM")


def part1(grid):
    count = 0
    for r, row in enumerate(grid):
        for c, let in enumerate(row):
            if let == 'X':
                count += check(grid, r, c, "XMAS")
            if let == 'S':
                count += check(grid, r, c, "SAMX")
    return count



def part2(grid):
    count = 0
    for r, row in enumerate(grid):
        for c, let in enumerate(row):
            if let == 'A':
                count += check2(grid, r, c)
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

