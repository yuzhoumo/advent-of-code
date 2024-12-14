import aoc
from time import sleep


def step(state, w, h):
    res = []
    for p, v in state:
        np = ((p[0] + v[0]) % w, (p[1] + v[1]) % h)
        res.append((np, v))
    return res


def safety(state, w, h):
    counts = [0, 0, 0, 0]
    for p, _ in state:
        if p[0] < w // 2 and p[1] < h // 2:
            counts[0] += 1
        elif p[0] > w // 2 and p[1] < h // 2:
            counts[1] += 1
        elif p[0] < w // 2 and p[1] > h // 2:
            counts[2] += 1
        elif p[0] > w // 2 and p[1] > h // 2:
            counts[3] += 1

    return counts[0] * counts[1] * counts[2] * counts[3]


def display(state, w, h):
    grid = [["."] * w for _ in range(h)]
    for p, _ in state:
        grid[p[1]][p[0]] = "X"
    for row in grid:
        print(''.join(row))


def part1(state):
    state = state.copy()
    for _ in range(100):
        state = step(state, 101, 103)
    return safety(state, 101, 103)


def part2(state):
    state = state.copy()
    for i in range(10000):
        points = [p for p, _ in state]
        if len(set(points)) == len(state):
            display(state, 101, 103)
            return i
        state = step(state, 101, 103)


def main(text):
    data = text.strip()
    state = []
    for row in data.splitlines():
        p, v = row.split()
        x, y = p.split(',')
        x, y = int(x[2:]), int(y)

        xv, yv = v.split(',')
        xv, yv = int(xv[2:]), int(yv)
        state.append(((x, y), (xv, yv)))

    return part1(state), part2(state)


if __name__ == "__main__":
    aoc.run(main, 14)
