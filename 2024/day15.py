import aoc

def dir(m):
    dr, dc = 0, 0
    match m:
        case '^': dr = -1
        case 'v': dr = 1
        case '<': dc = -1
        case '>': dc = 1
    return dr, dc


def move(grid, r, c, m):
    dr, dc = dir(m)
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == '.':
        grid[r][c] = '.'
        grid[nr][nc] = '@'
        return nr, nc

    cr, cc = nr, nc
    while grid[cr][cc] != '#':
        cr, cc = dr + cr, dc + cc
        if grid[cr][cc] == '.':
            grid[cr][cc] = 'O'
            grid[nr][nc] = '@'
            grid[r][c] = '.'
            return nr, nc

    return r, c


def move2(grid, r, c, m):
    dr, dc = dir(m)
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == '.':
        grid[r][c] = '.'
        grid[nr][nc] = '@'
        return nr, nc

    cr, cc = nr, nc
    while grid[cr][cc] != '#':
        cr, cc = dr + cr, dc + cc
        if grid[cr][cc] == '.':
            grid[cr][cc] = 'O'
            grid[nr][nc] = '@'
            grid[r][c] = '.'
            return nr, nc

    return r, c


def gps_sum(grid):
    res = 0
    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == 'O' or item == '[':
                res += r * 100 + c
    return res


def part1(grid, moves, pos):
    r, c = pos
    for m in moves:
        r, c = move(grid, r, c, m)
    return gps_sum(grid)


def part2(grid, moves, pos):
    r, c = pos
    for m in moves:
        r, c = move2(grid, r, c, m)
    return gps_sum(grid)


def main(text):
    data = text.strip()
    grid, moves = [], []
    pos = [0, 0]

    for r, line in enumerate(data.splitlines()):
        if '#' in line:
            if '@' in line: pos = [r, line.index('@')]
            grid.append(list(line))
        elif line.strip() != '':
            moves.extend(list(line))

    grid2 = []
    for row in grid:
        new_row = []
        for c in row:
            match c:
                case 'O': new_row.extend(['[', ']'])
                case '@': new_row.extend(['@', '.'])
                case '.': new_row.extend(['.', '.'])
                case '#': new_row.extend(['#', '#'])
            grid2.append(new_row)

    return part1(grid, moves, pos), part2(grid2, moves, pos)


if __name__ == "__main__":
    aoc.run(main, 15)
