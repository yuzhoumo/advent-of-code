import aoc
from collections import deque, defaultdict


def part1(grid):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    in_bounds = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def bfs(r, c):
        seen = set()
        dq = deque([(r, c)])

        count = 0
        while dq:
            r, c = dq.popleft()

            if (r, c) in seen:
                continue

            seen.add((r, c))

            if grid[r][c] == 9:
                count += 1
                continue

            for dr, dc in dirs:
                nr, nc  = r + dr, c + dc
                if in_bounds(nr, nc) and ((grid[nr][nc] - grid[r][c]) == 1):
                    dq.append((nr, nc))

        return count

    res = 0
    for r, row in enumerate(grid):
        for c, n in enumerate(row):
            if n == 0:
                res += bfs(r, c)

    return res



def part2(grid):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    in_bounds = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def dfs(r, c):
        if grid[r][c] == 9:
            return 1

        count = 0
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if in_bounds(nr, nc) and (grid[nr][nc] - grid[r][c]) == 1:
                count += dfs(nr, nc)

        return count

    res = 0
    for r, row in enumerate(grid):
        for c, n in enumerate(row):
            if n == 0:
                res += dfs(r, c)

    return res


def main(text):
    data = text.strip()
    grid = [[int(n) for n in row] for row in data.splitlines()]
    return part1(grid), part2(grid)


if __name__ == "__main__":
    aoc.run(main, 10)
