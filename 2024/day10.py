import aoc
from collections import deque


def bfs(grid, r, c, check_seen=True):
    seen = set()
    dq = deque([(r, c)])

    count = 0
    while dq:
        r, c = dq.popleft()

        if check_seen and (r, c) in seen:
            continue
        elif check_seen:
            seen.add((r, c))

        if grid[r][c] == 9:
            count += 1
            continue

        for dr, dc in aoc.directions:
            nr, nc  = r + dr, c + dc
            if aoc.in_bounds(grid, nr, nc) and (grid[nr][nc] - grid[r][c]) == 1:
                dq.append((nr, nc))

    return count


def part1(grid):
    res = 0
    for r, row in enumerate(grid):
        for c, n in enumerate(row):
            if n == 0:
                res += bfs(grid, r, c)
    return res


def part2(grid):
    res = 0
    for r, row in enumerate(grid):
        for c, n in enumerate(row):
            if n == 0:
                res += bfs(grid, r, c, check_seen=False)
    return res


def main(text):
    data = text.strip()
    grid = [[int(n) for n in row] for row in data.splitlines()]
    return part1(grid), part2(grid)


if __name__ == "__main__":
    aoc.run(main, 10)
