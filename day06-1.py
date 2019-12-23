import sys


class Tree:
    def __init__(self, label, branches=[], parent=None):
        self.label = label
        self.parent = parent
        self.branches = list(branches)

    def add_branch(self, b):
        self.branches.append(b)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.branches


def make_map(tree, orbits):
    for orbit in orbits:
        if orbit[0] == tree.label:
            tree.add_branch(Tree(orbit[1], parent=tree))
            orbits.remove(orbit)
    for b in tree.branches:
        make_map(b, orbits)


def count_orbits(tree):
    count, node = 0, tree
    while not node.is_root():
        node = node.parent
        count += 1
    for b in tree.branches:
        count += count_orbits(b)
    return count


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) < 3, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    orbital_map = Tree('COM')
    make_map(orbital_map, [line.strip().split(')') for line in f.readlines()])

print(count_orbits(orbital_map))
