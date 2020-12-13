import sys


# Part 1
def manhattan_dist1(instructions, start_bearing):
    """
    Takes a list of instructions and moves the ship accordingly. Returns the
    final manhattan distance from the origin. Instructions are a list of tuples
    of the format (direction: n). Instructions can be 'N', 'E', 'S', 'W', 'L',
    'R', and 'F' followed by an integer. The integer indicates how far to move
    for the cardinal directions and forwards ('F') or how many degrees to
    rotate for the left/right ('L', 'R') directions. Rotations can only be in
    90-degree increments. The ship starts out facing east.
    """

    # Map directions to their indices
    directions = { 'N': 0, 'E': 1, 'S': 2, 'W': 3 }
    moves, bearing = [0, 0, 0, 0], start_bearing

    for d, n in instructions:

        if d == 'L':
            # Turn left
            n = (n // 90) % 4
            bearing = (bearing + 3 * n) % 4
        elif d == 'R':
            # Turn right
            n = (n // 90) % 4
            bearing = (bearing + n) % 4
        elif d == 'F':
            # Move forward
            moves[bearing] += n
        else:
            # Move in the specified direction
            i = directions[d]
            moves[i] += n

    # Get final x, y coordinates and return distance
    x, y = moves[0] - moves[2], moves[1] - moves[3]
    return abs(x) + abs(y)


# Part 2
def manhattan_dist2(instructions, start_coords):
    """
    Takes a list of instructions of the same format as `manhattan_dist1` but
    with different interpretation. Each move alters the position of a waypoint
    (relative to the ship's position), and 'F' moves the ship to the waypoint
    the specified number of times. 'L' and 'R' rotate the waypoint around the
    ship counter-clockwise and clockwise respectively.
    """

    # Map directions to their indices
    directions = { 'N': 0, 'E': 1, 'S': 2, 'W': 3 }
    ship, moves = [0, 0], start_coords

    for d, n in instructions:

        if d == 'L':
            # Rotate waypoint left (counter-clockwise)
            n = (n // 90) % 4
            moves = moves[n:] + moves[:n]
        elif d == 'R':
            # Turn waypoint right (clockwise)
            n = (n // 90) % 4
            moves = moves[-n:] + moves[:-n]
        elif d == 'F':
            # Move ship to the waypoint n times
            ship[0] += n * (moves[0] - moves[2])
            ship[1] += n * (moves[1] - moves[3])
        else:
            # Move waypoint in the specified direction
            i = directions[d]
            moves[i] += n

    # Get final x, y coordinates and return distance
    return abs(ship[0]) + abs(ship[1])


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        instructions = [(row[:1], int(row[1:])) for row in text.splitlines()]

    # Solve part 1
    initial_bearing = 1  # Ship starts facing east
    part1 = manhattan_dist1(instructions, initial_bearing)
    print('\nPart 1:', part1)

    # Solve part 2
    initial_waypoint = [1, 10, 0, 0]  # Waypoint starts at N1, E10
    part2 = manhattan_dist2(instructions, initial_waypoint)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
