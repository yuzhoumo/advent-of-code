import aoc
from collections import deque


def part1(grid):
    seen = set()

    def bfs(r, c):
        let = grid[r][c]
        dq = deque([(r, c)])
        area = perimeter = 0

        while dq:
            r, c = dq.popleft()
            if (r, c) in seen:
                continue

            seen.add((r, c))
            area += 1

            perimeter += 4
            for dr, dc in aoc.directions:
                nr, nc = r + dr, c + dc
                if aoc.in_bounds(grid, nr, nc) and grid[nr][nc] == let:
                    perimeter -= 1
                    dq.append((nr, nc))

        return perimeter, area

    cost = 0
    for r, row in enumerate(grid):
        for c in range(len(row)):
            if (r, c) in seen:
                continue
            p, a = bfs(r, c)
            cost += p * a

    return cost


def part2(grid):
    pass


def main(text):
    data = text.strip()
    grid = [list(row) for row in data.splitlines()]
    return part1(grid), part2(grid)


if __name__ == "__main__":
    aoc.run(main, 12)
