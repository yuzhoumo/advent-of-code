import unittest
import day01_1 as p1
import day01_2 as p2


class TestDay1(unittest.TestCase):
    def test_part1(self):
        tests = [(12, 2),
                 (14, 2),
                 (1969, 654),
                 (100756, 33583)]

        for t in tests:
            self.assertEqual(p1.calc_fuel(t[0]), t[1])

    def test_part2(self):
        tests = [(14, 2),
                 (1969, 966),
                 (100756, 50346)]

        for t in tests:
            self.assertEqual(p2.calc_fuel(t[0]), t[1])


if __name__ == '__main__':
    unittest.main()
