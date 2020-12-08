import sys
import re

# Part 1
def count_trees(grid, rise, run):
    r, c, cnt = 0, 0, 0
    rows, cols = len(grid), len(grid[0])

    while r < len(grid):
        cnt += grid[r % rows][c % cols] == '#'
        r, c = r + rise, c + run

    return cnt


# Part 2
def count_product(grid, slopes):
    product = 1

    for slope in slopes:
        product *= count_trees(grid, slope[0], slope[1])

    return product


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        rows = text.splitlines()

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', count_trees(rows, 1, 3))

    # Part 2 slopes
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    print('\nPart 2:', count_product(rows, slopes))

if __name__ == '__main__':
    main()
