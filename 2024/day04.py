import aoc


def search(grid, r, c, word):
    count, n = 0, len(word)

    # horizontal
    if c + n <= len(grid[0]):
        count += ''.join(grid[r][c:c+n]) == word

    # vertical
    if r + n <= len(grid):
        count += ''.join(grid[r+i][c] for i in range(n)) == word

    # diagonal down
    if (c + n <= len(grid[0])) and (r + n <= len(grid)):
        count += ''.join(grid[r+i][c+i] for i in range(n)) == word

    # diagonal up
    if (c + n <= len(grid[0])) and (r - n + 1 >= 0):
        count += ''.join(grid[r-i][c+i] for i in range(n)) == word

    return count


def search2(grid, r, c):
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
                count += search(grid, r, c, "XMAS")
            elif let == 'S':
                count += search(grid, r, c, "SAMX")
    return count

def part2(grid):
    count = 0
    for r, row in enumerate(grid):
        for c, let in enumerate(row):
            if let == 'A':
                count += search2(grid, r, c)
    return count


def main(text, part=None):
    data = text.strip()
    grid = [list(row) for row in data.splitlines()]

    if part is None or part == 1:
        print(f"part 1: {part1(grid)}")
    if part is None or part == 2:
        print(f"part 2: {part2(grid)}")


if __name__ == "__main__":
    aoc.run(main, 4)

