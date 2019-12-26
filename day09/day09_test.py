import os
import unittest
import sys
import day09_1 as p1
import day09_2 as p2


class TestDay9(unittest.TestCase):
    def test_part1(self):
        tests = [((109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99),
                  (109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99)),

                 ((1102, 34915192, 34915192, 7, 4, 7, 99, 0), (1219070632396864,)),

                 ((104, 1125899906842624, 99), (1125899906842624,))]

        sys.stdout = open(os.devnull, 'w')  # Block print statements from displaying

        for t in tests:
            user_input, memory = [1], t[0]
            output = p1.IntComputer(user_input, memory).run()
            self.assertEqual(tuple(output), t[1])

        sys.stdout.close()
        sys.stdout = sys.__stdout__  # Unblock print statements

    def test_part2(self):
        tests = [((109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99),
                  (109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99)),

                 ((1102, 34915192, 34915192, 7, 4, 7, 99, 0), (1219070632396864,)),

                 ((104, 1125899906842624, 99), (1125899906842624,))]

        sys.stdout = open(os.devnull, 'w')  # Block print statements from displaying

        for t in tests:
            user_input, memory = [1], t[0]
            output = p2.IntComputer(user_input, memory).run()
            self.assertEqual(tuple(output), t[1])

        sys.stdout.close()
        sys.stdout = sys.__stdout__  # Unblock print statements


if __name__ == '__main__':
    unittest.main()
