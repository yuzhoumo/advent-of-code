import sys

""" Day 6: Universal Orbit Map (Part 1)

Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding
efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input). Except
for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object.

Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can be any number of objects long: if A
orbits B, B orbits C, and C orbits D, then A indirectly orbits D. What is the total number of direct and indirect
orbits in your map data? """


class Tree:
    def __init__(self, label, branches=[], parent=None):
        self.label = label
        self.parent = parent
        self.branches = list(branches)

    def add_branch(self, b):
        self.branches.append(b)

    def is_root(self):
        return self.parent is None


def make_map(tree, orbits):
    for orbit in orbits:  # orbits is a list of string pairs ['AAA', 'BBB'] where 'BBB' orbits 'AAA'
        if orbit[0] == tree.label:
            tree.add_branch(Tree(orbit[1], parent=tree))
            orbits.remove(orbit)
    for b in tree.branches:
        make_map(b, orbits)


def count_orbits(tree):
    count, node = 0, tree
    while not node.is_root():  # Counts number of orbits between given node and root
        node = node.parent
        count += 1
    for b in tree.branches:
        count += count_orbits(b)
    return count


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        orbital_map, orbits = Tree('COM'), [orbit.strip().split(')') for orbit in f.readlines()]
        make_map(orbital_map, orbits)

    print(count_orbits(orbital_map))


if __name__ == '__main__':
    main()
