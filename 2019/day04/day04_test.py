import unittest
import day04_1 as p1
import day04_2 as p2


class TestDay3(unittest.TestCase):
    def test_part1(self):
        f = p1.is_valid_password
        tests = [(122345, True),
                 (111123, True),
                 (111111, True),
                 (223450, False),
                 (123789, False)]

        for t in tests:
            self.assertEqual(f(t[0]), t[1])

    def test_part2(self):
        f, adj = p2.is_valid_password, tuple(0 for _ in range(0, 10))
        tests = [(112233, True),
                 (111122, True),
                 (123444, False)]

        for t in tests:
            self.assertEqual(f(t[0], list(adj)), t[1])


if __name__ == '__main__':
    unittest.main()
