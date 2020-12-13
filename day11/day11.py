import sys


# Shared bewteen part 1 and 2
ADJ = ((-1, -1), (-1, 00), (-1, +1),
       (00, -1),           (00, +1),
       (+1, -1), (+1, 00), (+1, +1))


def get_next_state(seats, rules):
    """
    Takes in a 2D array of characters representing seats and gets the next
    state of the system given a dictionary of rules.
    """

    next_state, changes = [], 0
    for i in range(len(seats)):
        next_state.append([])
        for j in range(len(seats[0])):
            seat = rules[seats[i][j]](seats, i, j)
            changes += seat != seats[i][j]
            next_state[i].append(seat)

    return next_state, changes


def occupied_seats(seats, rules):
    """
    Counts the number of occupied seats that will eventually be reached when
    the state of the system reaches equilibrium.
    """

    state, changes = get_next_state(seats, rules)
    while changes != 0:
        state, changes = get_next_state(state, rules)

    return sum(seat == '#' for row in state for seat in row)


# Part 1
def check_adj(seats, r, c):
    """
    Takes a 2D array of characters and returns the number of occupied seats
    (represented by '#') that are adjacent to a given seat.
    """

    occupied = 0
    for dr, dc in ADJ:

        i, j = r + dr, c + dc
        in_bounds = 0 <= i < len(seats) and 0 <= j < len(seats[0])

        if in_bounds and seats[i][j] == '#':
            occupied += 1

    return occupied


# Part 2
def check_vis(seats, r, c):
    """
    Takes a 2D array of characters and returns the number of occupied seats
    (represented by '#') that are visible to a given seat (ie. count the first
    seat that is encountered after moving in a straight line in any of the
    adjacent directions).
    """

    occupied = 0
    for dr, dc in ADJ:
        i, j = r + dr, c + dc
        while 0 <= i < len(seats) and 0 <= j < len(seats[0]):

            if seats[i][j] == '#':
                occupied += 1
                break
            elif seats[i][j] == 'L':
                break

            i, j = i + dr, j + dc

    return occupied


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        seats = [list(row) for row in text.splitlines()]

    # Rules for state changes
    rules1 = {
        'L': lambda seats, i, j: '#' if check_adj(seats, i, j) == 0 else 'L',
        '#': lambda seats, i, j: 'L' if check_adj(seats, i, j) >= 4 else '#',
        '.': lambda seats, i, j: '.'
    }

    rules2 = {
        'L': lambda seats, i, j: '#' if check_vis(seats, i, j) == 0 else 'L',
        '#': lambda seats, i, j: 'L' if check_vis(seats, i, j) >= 5 else '#',
        '.': lambda seats, i, j: '.'
    }

    # Solve for parts 1 and 2
    print('\nPart 1:', occupied_seats(seats, rules1))
    print('Part 2:', occupied_seats(seats, rules2))


if __name__ == '__main__':
    main()
