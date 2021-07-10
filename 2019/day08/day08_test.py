import unittest
import day08_1 as p1
import day08_2 as p2


class TestDay8(unittest.TestCase):
    def test_part1(self):
        tests = [('123456789012', 3, 2, 1), ('101101', 3, 1, 0), ('120021020102', 2, 2, 2)]

        for t in tests:
            raw_data, x_dim, y_dim = t[0], t[1], t[2]

            image = p1.Image(x_dim, y_dim)
            image.set_data(raw_data)
            result = p1.corruption_check(image)

            self.assertEqual(result, t[3])

    def test_part2(self):
        tests = [('0222112222120000', 2, 2, '░█\n█░'), ('100020012010202202012012212', 3, 3, '█░░\n░░░\n░█ ')]

        for t in tests:
            raw_data, x_dim, y_dim = t[0], t[1], t[2]
            image = p2.Image(x_dim, y_dim)
            image.set_data(raw_data)
            result = image.decode()

            self.assertEqual(str(result), t[3])


if __name__ == '__main__':
    unittest.main()
