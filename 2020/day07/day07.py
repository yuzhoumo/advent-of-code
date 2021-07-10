import sys
import re
from functools import lru_cache


RULES = {}  # Global variable for storing bag rules, set in main


def parse_input(descriptions):
    """
    Parses the input descriptions into a usable data structure. `rules` is a
    dictionary of the following structure:

    rules = { 

        'yellow': {
            'brown': 3,
            'black': 2
        },
        
        ...

    }

    The keys of the top level dictionary are bag colors and the values are
    sub-dictionaries that list its required children as (bag color: amount).
    """

    rules = {}

    for line in descriptions:
        bag, children = line.split(' bags contain ')
        children = re.compile(r'([0-9]+) ([a-z]+ [a-z]+)').findall(children)
        rules[bag] = { color: int(n) for n, color in children }

    return rules


# Part 1
@lru_cache(maxsize=128)
def search_bags(start, target):
    """
    Returns True if a bag of color `start` will eventually contain a child bag
    of color `target`, False otherwise.
    """

    children = RULES[start]

    if children is None:
        return False

    if target in children:
        return True

    for color in children:
        if search_bags(color, target):
            return True

    return False


# Part 2
@lru_cache(maxsize=128)
def count_bags(root):
    """
    Counts the number of total sub-bags given global `RULES` and a bag of
    color `root`.
    """

    children = RULES[root]

    if children is None:
        return 1

    # Number of bags in the current level
    count = sum(children.values())

    for key in children.keys():
        count += children[key] * count_bags(key)

    return count


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    global RULES  # Use global variable for rules to support LRU cache

    with open(input_file, 'r') as f:
        descriptions = f.read().splitlines()

    # Set global rules for bag colors
    RULES = parse_input(descriptions)
    colors = RULES.keys()

    # Solve part 1
    part1 = sum(1 for c in colors if search_bags(c, 'shiny gold'))
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = count_bags('shiny gold')
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
