import aoc


def in_bound(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def step(grid, dir, gr, gc):
    nr, nc = gr, gc
    match dir:
        case 0: nr, nc = gr - 1, gc # up
        case 1: nr, nc = gr, gc + 1 # right
        case 2: nr, nc = gr + 1, gc # down
        case 3: nr, nc = gr, gc - 1 # left
        case _: raise ValueError("bad direction") # sanity check
    if in_bound(grid, nr, nc) and grid[nr][nc] == "#":
        return (dir + 1) % 4, gr, gc
    return dir, nr, nc


def get_unique_positions(grid, start):
    dir, gr, gc = 0, start[0], start[1]
    unique = set()
    while in_bound(grid, gr, gc):
        unique.add((gr, gc))
        dir, gr, gc = step(grid, dir, gr, gc)
    return unique


def detect_cycle(grid, start):
    # Floyd's cycle finding algorithm
    sdir, sr, sc = 0, start[0], start[1]
    fdir, fr, fc = 0, start[0], start[1]
    while in_bound(grid, fr, fc):
        sdir, sr, sc = step(grid, sdir, sr, sc)
        fdir, fr, fc = step(grid, fdir, fr, fc)
        fdir, fr, fc = step(grid, fdir, fr, fc)
        if (fdir, fr, fc) == (sdir, sr, sc):
            return True
    return False


def part1(positions):
    return len(positions)


def part2(grid, start, positions):
    count = 0
    for r, c in positions:
        grid[r][c] = "#"
        if detect_cycle(grid, start):
            count += 1
        grid[r][c] = "."
    return count


def main(text):
    data, grid, start = text.strip(), [], None
    for r, row in enumerate(data.splitlines()):
        grid.append(list(row))
        if '^' in row:
            start = (r, row.index('^'))

    positions = get_unique_positions(grid, start)
    sol1 = part1(positions)

    positions.remove(start)
    sol2 = part2(grid, start, positions)

    return sol1, sol2


if __name__ == "__main__":
    aoc.run(main, 6)
