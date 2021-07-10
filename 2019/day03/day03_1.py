import sys

""" Day 3: Crossed Wires (Part 1)
Two wires are connected to a central port and extend outward on a grid.
You trace the path each wire takes as it leaves the central port, one
wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths.
To fix the circuit, you need to find the intersection point closest to
the central port. Because the wires are on a grid, use the Manhattan
distance for this measurement. While the wires do technically cross
right at the central port where they both start, this point does not
count, nor does a wire count as crossing with itself. What is the
Manhattan distance from the central port to the closest
intersection? """


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def taxi_dist(self, other):
        # Returns manhattan distance between 2 points
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)


class Line:
    def __init__(self, a, b):
        assert isinstance(a, Point), ('Endpoint a is not a valid point '
                                      'object')
        assert isinstance(a, Point), ('Endpoint b is not a valid point '
                                      'object')
        # Sets endpoints of line
        self.a, self.b = a, b

    def get_intersect(self, other):
        # Determines vertical or horizontal lines assuming line segments
        # are parallel to either x or y axes
        if self.a.x == self.b.x and other.a.y == other.b.y:
            horizontal = (self.a.x, (self.a.y, self.b.y))
            vertical = (other.a.y, (other.a.x, other.b.x))
        elif self.a.y == self.b.y and other.a.x == other.b.x:
            vertical = (other.a.x, (other.a.y, other.b.y))
            horizontal = (self.a.y, (self.a.x, self.b.x))
        else:
            # Lines are parallel to each other or one or both are not
            # parallel to either x or y axes
            return None  

        # Returns intersection point if it exists, otherwise None
        x, y = vertical[0], horizontal[0]
        if min(horizontal[1]) < x < max(horizontal[1]) and \
                min(vertical[1]) < y < max(vertical[1]):
            return Point(x, y)

    def __repr__(self):
        return 'Line({0}, {1})'.format(repr(self.a), repr(self.b))


def gen_points(instructions):
    points = [Point(0, 0)]  # Sets first point to origin

    for instruction in instructions:
        # Gets coordinates of previous point
        prev_x, prev_y = points[-1].x, points[-1].y
        # Gets direction and distance value
        direction, dist = instruction[0], int(instruction[1:])

        # Sets next point based on direction & distance from prev point
        if direction == 'U':  # Up
            points.append(Point(prev_x, prev_y + dist))
        elif direction == 'D':  # Down
            points.append(Point(prev_x, prev_y - dist))
        elif direction == 'L':  # Left
            points.append(Point(prev_x - dist, prev_y))
        elif direction == 'R':  # Right
            points.append(Point(prev_x + dist, prev_y))
        else:  # Error if direction is not U, D, L, or R
            raise ValueError('Malformed instructions')

    return points


def gen_lines(points):
    # Generates a list of line objects based on a list of endpoints
    lines = []
    for i in range(len(points) - 1):
        lines.append(Line(points[i], points[i + 1]))
    return lines


def intersects(lines1, lines2):
    # Note: Assumes both lines consist of segments parallel to either
    # x or y axes
    results = []
    for first in lines1:
        for second in lines2:
            intersect = first.get_intersect(second)
            if intersect:
                results.append(intersect)
    return results


def closest_dist(origin, points):
    return min(origin.taxi_dist(p) for p in points)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        instructions = f.readlines()

    # Read instructions for two wires from input file
    instructions1 = instructions[0].split(',')
    instructions2 = instructions[1].split(',')

    line1 = gen_lines(gen_points(instructions1))
    line2 = gen_lines(gen_points(instructions2))

    intersections = intersects(line1, line2)

    print(closest_dist(Point(0, 0), intersections))


if __name__ == '__main__':
    main()
