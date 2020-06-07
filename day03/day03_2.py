import sys

""" Day 3: Crossed Wires (Part 2)
It turns out that this circuit is very timing-sensitive; you actually
need to minimize the signal delay. To do this, calculate the number of
steps each wire takes to reach each intersection; choose the
intersection where the sum of both wires' steps is lowest. If a wire
visits a position on the grid multiple times, use the steps value from
the first time it visits that position when calculating the total value
of a specific intersection. """


def points(instructions):
    # Return dictionary of points in the form 
    # {(x, y): min_cumulative_distance}

    def intermediary_points(prev, length, direction):
        # Gets a list of all the points on a line
        if direction == 'R':
            points = [(prev[0] + i, prev[1], prev[2] + i)
                      for i in range(1, length + 1)]
        elif direction == 'L':
            points = [(prev[0] - i, prev[1], prev[2] + i)
                      for i in range(1, length + 1)]
        elif direction == 'U':
            points = [(prev[0], prev[1] + i, prev[2] + i)
                      for i in range(1, length + 1)]
        elif direction == 'D':
            points = [(prev[0], prev[1] - i, prev[2] + i)
                      for i in range(1, length + 1)]
        else:
            assert False, 'Invalid instructions.'
        return points

    # Point tuples are in the format: (x, y, cumulative_length)
    prev, result = (0, 0, 0), {}

    for element in instructions:
        direction, length = element[0], int(element[1:])
        points = intermediary_points(prev, length, direction)

        for curr in points:  # Convert into dictionary entries
            result[curr[:2]] = min(result[curr[:2]], curr[2]) if curr[:2] in \
                               result else curr[2]

        prev = points[-1]

    return result


def intersections(locations1, locations2):
    # Return tuple set of intersections of points in dictionaries
    points1, points2 = set(locations1.keys()), set(locations2.keys())
    return tuple(points1.intersection(points2))


def min_cumulative_sum(intersections, locations1, locations2):
    # Return the min sum of cumulative lengths at the intersections
    lengths = [locations1[point] + locations2[point]
               for point in intersections]
    return min(lengths)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        instructions = f.readlines()

    # Read instructions for two wires from input file
    instructions1 = instructions[0].split(',')
    instructions2 = instructions[1].split(',')

    # Get locations and calculate result
    points1 = points(instructions1)
    points2 = points(instructions2)
    overlaps = intersections(points1, points2)
    print(min_cumulative_sum(overlaps, points1, points2))


if __name__ == '__main__':
    main()
