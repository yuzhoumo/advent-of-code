import os
import unittest
import sys
import day05_1 as p1
import day05_2 as p2


class TestDay5(unittest.TestCase):
    def test_part1(self):
        tests = [((1101, 100, -1, 4, 0), (1101, 100, -1, 4, 99))]

        for t in tests:
            user_input, memory = [1], t[0]
            result = tuple(p1.IntComputer(user_input, memory).run())
            self.assertEqual(result, t[1])

    def test_part2(self):
        tests = [((3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8), 0),

                 ((3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8), 1),

                 ((3, 3, 1108, -1, 8, 3, 4, 3, 99), 0),

                 ((3, 3, 1107, -1, 8, 3, 4, 3, 99), 1),

                 ((3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9), 1),

                 ((3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1), 1),

                 ((3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21,
                   125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99),
                  999)]

        sys.stdout = open(os.devnull, 'w')  # Block print statements from displaying

        for t in tests:
            user_input, memory = [5], t[0]
            result = p2.IntComputer(user_input, memory).run()[0]
            self.assertEqual(result, t[1])

        sys.stdout.close()
        sys.stdout = sys.__stdout__  # Unblock print statements


if __name__ == '__main__':
    unittest.main()
