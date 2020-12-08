import sys

# Part 1
def count_trees(grid, rise, run):
    """
    Given a slope and starting from the top left corner, count
    number of tree collisions on the map `grid`, which is a list
    of strings where '#' represents a tree. The grid pattern repeats
    horizontally and the function ends upon hitting the bottom row
    of the grid.
    """

    r, c, cnt = 0, 0, 0
    rows, cols = len(grid), len(grid[0])

    while r < len(grid):
        cnt += grid[r % rows][c % cols] == '#'
        r, c = r + rise, c + run

    return cnt


# Part 2
def count_product(grid, slopes):
    """
    Given a map `grid` and a list of slopes, perform `count_trees`
    on each slope to get the number of tree collisions, and return
    the product of all of the results.
    """

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
        grid = text.splitlines()

    # Solve part 1 and 2
    part1 = count_trees(grid, 1, 3)
    part2 = count_product(grid, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', part1)
    print('\nPart 2:', part2)


if __name__ == '__main__':
    main()
