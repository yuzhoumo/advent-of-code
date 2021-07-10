import sys

# Part 1
def count_trees(layout, rise, run):
    """
    Given a slope and starting from the top left corner (0, 0), count the number
    of tree collisions on the map `layout`, which is a list of strings where '#'
    represents a tree. The layout pattern repeats horizontally and the function
    ends upon hitting the bottom row of the layout.
    """

    r, c, trees = 0, 0, 0
    rows, cols = len(layout), len(layout[0])

    while r < len(layout):
        trees += layout[r % rows][c % cols] == '#'
        r, c = r + rise, c + run

    return trees


# Part 2
def count_trees_product(layout, slopes):
    """
    Given a map `layout` and a list of slopes, perform `count_trees` on each
    slope to get the number of tree collisions, and return the product of all
    of the results.
    """

    product = 1

    for slope in slopes:
        product *= count_trees(layout, slope[0], slope[1])

    return product


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        layout = f.read().splitlines()

    # Solve part 1
    part1 = count_trees(layout, 1, 3)
    print('\nPart 1:', part1)

    # Solve part 2
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    part2 = count_trees_product(layout, slopes)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
