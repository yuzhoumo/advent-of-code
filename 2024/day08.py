import aoc
from collections import defaultdict


def part1(antennas, in_bound):
    antinodes = set()

    def get_antinodes(p, pi):
        if p == pi:
            return

        for p1, p2 in ((p, pi), (pi, p)):
            dr, dc = p1[0] - p2[0], p1[1] - p2[1]
            nr, nc = p1[0] + dr, p1[1] + dc
            if in_bound(nr, nc):
                antinodes.add((nr, nc))

    for a, points in antennas.items():
        for p in points:
            for pi in antennas[a]:
                get_antinodes(p, pi)

    return len(antinodes)


def part2(antennas, in_bound):
    antinodes = set()

    def get_antinodes(p, pi):
        if p == pi:
            antinodes.add(p)
            return

        for p1, p2 in ((p, pi), (pi, p)):
            dr, dc = p1[0] - p2[0], p1[1] - p2[1]
            nr, nc = p1[0] + dr, p1[1] + dc
            while in_bound(nr, nc):
                antinodes.add((nr, nc))
                nr += dr
                nc += dc

    for a, points in antennas.items():
        for p in points:
            for pi in antennas[a]:
                get_antinodes(p, pi)

    return len(antinodes)


def main(text):
    data = text.strip()
    grid = [list(row) for row in data.splitlines()]
    in_bound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])

    antennas = defaultdict(list)
    for r, row in enumerate(grid):
        for c, a in enumerate(row):
            if a == '.': continue
            antennas[a].append((r, c))

    return part1(antennas, in_bound), part2(antennas, in_bound)


if __name__ == "__main__":
    aoc.run(main, 8)
