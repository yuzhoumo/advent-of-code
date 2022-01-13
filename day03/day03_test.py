import unittest
import day03_1 as p1


class TestDay3(unittest.TestCase):
    def test_part1(self):
        tests = [(('R8', 'U5', 'L5', 'D3'),
                  ('U7', 'R6', 'D4', 'L4'), 6),

                 (('R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'),
                  ('U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'), 159),

                 (('R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'),
                  ('U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'), 135)]

        for t in tests:
            line1, line2 = p1.gen_lines(p1.gen_points(t[0])), p1.gen_lines(p1.gen_points(t[1]))
            intersections = p1.intersects(line1, line2)
            result = p1.closest_dist(p1.Point(0, 0), intersections)

            self.assertEqual(result, t[2])


if __name__ == '__main__':
    unittest.main()
