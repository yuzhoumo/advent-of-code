import sys

""" Day 6: Universal Orbit Map

Figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN). You start at the object YOU are
orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object
orbiting or orbited by that object. What is the minimum number of orbital transfers required to move from the object YOU
are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.) """


class Tree:
    def __init__(self, label, branches=[], parent=None):
        self.label = label
        self.parent = parent
        self.branches = list(branches)

    def add_branch(self, b):
        self.branches.append(b)

    def is_root(self):
        return self.parent is None


def make_map(tree, orbits, poi=[]):
    # orbits is a list of string pairs ['AAA', 'BBB'] where 'BBB' orbits 'AAA'
    # poi is a list of strings to replace with nodes of those points of interest when created
    for orbit in orbits:
        if orbit[0] == tree.label:
            new_node = Tree(orbit[1], parent=tree)
            tree.add_branch(new_node)
            if orbit[1] in poi:  # Replaces string with node indicated by string when the node is created
                poi.remove(orbit[1])
                poi.append(new_node)
    for b in tree.branches:
        make_map(b, orbits, poi)


def find_dist(node1, node2):  # node1 and node2 must be in the same tree
    lst1, lst2 = [], []
    while not node1.parent.is_root():  # Makes list of nodes on path from node1 to root node
        node1 = node1.parent
        lst1.append(node1)
    while not node2.parent.is_root():  # Makes list of nodes on path from node2 to root node
        node2 = node2.parent
        lst2.append(node2)

    # Finds lowest common ancestor on paths of both nodes to the root
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] is lst2[j]:  # Lowest common ancestor is found
                return i + j  # Returns number of nodes between node1 and common + number between node2 and common


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        orbital_map, points_of_interest = Tree('COM'), ['YOU', 'SAN']
        # Mutates points_of_interests to include nodes instead of strings
        make_map(orbital_map, [line.strip().split(')') for line in f.readlines()], points_of_interest)

    print(find_dist(points_of_interest[0], points_of_interest[1]))


if __name__ == '__main__':
    main()
