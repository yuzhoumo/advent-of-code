import unittest
import day06_1 as p1
import day06_2 as p2


class TestDay6(unittest.TestCase):
    def test_part1(self):
        tests = [[[['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'],
                   ['E', 'J'], ['J', 'K'], ['K', 'L']], 42]]

        for t in tests:
            orbital_map = p1.Tree('COM')
            p1.make_map(orbital_map, t[0])
            result = p1.count_orbits(orbital_map)
            self.assertEqual(result, t[1])

    def test_part2(self):
        tests = [[[['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'],
                   ['E', 'J'], ['J', 'K'], ['K', 'L'], ['K', 'YOU'], ['I', 'SAN']], 4]]

        for t in tests:
            orbital_map, points_of_interest = p2.Tree('COM'), ['YOU', 'SAN']
            p2.make_map(orbital_map, t[0], points_of_interest)
            result = p2.find_dist(points_of_interest[0], points_of_interest[1])
            self.assertEqual(result, t[1])


if __name__ == '__main__':
    unittest.main()
