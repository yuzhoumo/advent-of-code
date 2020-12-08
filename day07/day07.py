import sys
import re


def parse_input(lines):
    """
    Parses the input lines into a usable data structure. `rules` is a dict
    of the following structure:

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

    for line in lines:
        root, children = line.split(' bags contain ')
        children = re.compile(r'([0-9]+) ([a-z]+ [a-z]+)').findall(children)
        rules[root] = { color: int(n) for n, color in children }

    return rules


# Part 1
def search_bags(rules, root, color):
    """
    Returns True if a bag of color `root` will eventually contain a child bag
    of color `color`, False otherwise.
    """

    children = rules[root]

    if children is None:
        return False

    if color in children:
        return True

    for c in children:
        if search_bags(rules, c, color):
            return True

    return False


# Part 2
def count_bags(rules, root):
    """
    Counts the number of total sub-bags given `rules` and a bag of color `root`.
    """

    children = rules[root]

    if children is None:
        return 1

    count = sum(children.values())
    for key in children.keys():
        count += children[key] * count_bags(rules, key)

    return count


def main():

    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        lines = text.splitlines()
        rules = parse_input(lines)
        colors = rules.keys()

    # Solve for parts 1 and 2
    part1 = sum(1 for c in colors if search_bags(rules, c, 'shiny gold')) - 1
    part2 = count_bags(rules, 'shiny gold')

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', part1)
    print('\nPart 2:', part2)


if __name__ == '__main__':
    main()