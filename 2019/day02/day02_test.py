import unittest
import day02_1 as p1
import day02_2 as p2


class TestDay2(unittest.TestCase):
    def test_part1(self):
        tests = [((1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50), (3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50))]

        for t in tests:
            memory = t[0]
            result = tuple(p1.IntComputer(memory).run())
            self.assertEqual(result, t[1])

    def test_part2(self):
        f = p2.find_inputs
        tests = [(([1, 0, 0, 3, 2, 3, 11, 0, 99, 30, 40, 50] + [99 for _ in range(0, 88)]), 3500, 910)]

        for t in tests:
            expected, memory = t[1], t[0]
            self.assertEqual(f(expected, memory), t[2])


if __name__ == '__main__':
    unittest.main()
