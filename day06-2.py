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


def make_map(tree, orbits, poi=[]):
    for orbit in orbits:
        if orbit[0] == tree.label:
            new_node = Tree(orbit[1], parent=tree)
            tree.add_branch(new_node)
            if orbit[1] in poi:
                poi.remove(orbit[1])
                poi.append(new_node)
            orbits.remove(orbit)
    for b in tree.branches:
        make_map(b, orbits, poi)


def find_dist(node1, node2):
    lst1, lst2 = [], []
    while not node1.parent.is_root():
        node1 = node1.parent
        lst1.append(node1)
    while not node2.parent.is_root():
        node2 = node2.parent
        lst2.append(node2)

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] is lst2[j]:
                return i + j


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) < 3, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    orbital_map, points_of_interest = Tree('COM'), ['YOU', 'SAN']
    make_map(orbital_map, [line.strip().split(')') for line in f.readlines()], points_of_interest)

print(find_dist(points_of_interest[0], points_of_interest[1]))
