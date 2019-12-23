import sys


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def taxi_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self):
        return 'P<{0} {1}>'.format(self.x, self.y)


class Line:
    def __init__(self, point1, point2):
        self.a, self.b = point1, point2

    def get_intersect(self, other):
        if self.a.x == self.b.x:
            horizontal = (self.a.x, tuple(sorted([self.a.y, self.b.y])))
            vertical = (other.a.y, tuple(sorted([other.a.x, other.b.x])))
        else:
            vertical = (other.a.x, tuple(sorted([other.a.y, other.b.y])))
            horizontal = (self.a.y, tuple(sorted([self.a.x, self.b.x])))

        x, y = None, None

        if horizontal[1][0] < vertical[0] < horizontal[1][1]:
            x = vertical[0]
        if vertical[1][0] < horizontal[0] < vertical[1][1]:
            y = horizontal[0]

        if x is None and y is None:
            return Point(x, y)

    def __repr__(self):
        return 'L[{0} {1}]'.format(self.a, self.b)


def gen_points(wire):
    points = [Point(0,0)]

    for d in wire:
        prev_x, prev_y = points[-1].x, points[-1].y
        direction, dist = d[0], int(d[1:])

        if direction == 'U':
            points.append(Point(prev_x, prev_y + dist))
        elif direction == 'D':
            points.append(Point(prev_x, prev_y - dist))
        elif direction == 'L':
            points.append(Point(prev_x - dist, prev_y))
        elif direction == 'R':
            points.append(Point(prev_x + dist, prev_y))
        else:
            raise ValueError('Malformed instructions')

    return points


def gen_lines(points):
    lines = []
    for i in range(len(points) - 1):
        lines.append(Line(points[i], points[i+1]))
    return lines


def intersects(lines1, lines2):
    results = []
    for i in lines1:
        for j in lines2:
            temp = i.get_intersect(j)
            if temp:
                results.append(temp)
    return results


def closest_dist(origin, points):
    distances = [origin.taxi_dist(p) for p in points]
    return min(list(distances))


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) < 3, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    wires = f.readlines()

w1, w2 = wires[0].split(','), wires[1].split(',')
L1, L2 = gen_lines(gen_points(w1)), gen_lines(gen_points(w2))

intersections = intersects(L1, L2)
print(closest_dist(Point(0, 0), intersections))
