import sys

# Part 1
def get_id(code):
    """
    Given `code`, a string representing a boarding pass seat code,
    convert into a seat id, where `code` is a base 2 number such
    that 'B' -> 1, 'F' -> 0, 'R' -> 1, 'L' -> 0.

    Example: 'BFFFBBFRRR' -> 0b1000110111
        >>> get_id('BFFFBBFRRR')
        >>> 567
    """

    n, tot = 1, 0
    for c in code[::-1]:
        if c == 'B' or c == 'R':
            tot += n
        n *= 2

    return tot


# Part 2
def get_missing(seat_ids):
    """
    Given an unsorted list of consecutive seat ids, get the missing
    seat, where it is the only non-consecutive gap in the list (assume
    this number exists exactly once), return None otherswise.

    Example:
        >>> get_missing([1, 4, 3, 5])
        >>> 2
    """

    seat_ids = sorted(seat_ids)
    curr = seat_ids[0]

    for n in seat_ids:
        if curr != n:
            return curr
        curr += 1


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        seats = text.splitlines()

    # Get list of seat ids
    seat_ids = [get_id(s) for s in seats]

    # Solve parts 1 and 2
    part1 = max(seat_ids)
    part2 = get_missing(seat_ids)

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', part1)
    print('\nPart 2:', part2)


if __name__ == '__main__':
    main()
