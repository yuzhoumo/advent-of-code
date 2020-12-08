import sys
import re


# Part 1
def is_valid_count(rule):
    """
    Returns True if password contains at least the minimum and at
    most the maximum of a specified character, False otherwise.

    Example: ensure password contains between 1-13 'r' chars
        >>> is_valid_count('1-13 r: gqdrspndrpsrjfjx')
        >>> True
    """

    p = re.compile('[-: ]+')
    lo, hi, c, password = p.split(rule)
    cnt = password.count(c)
    return cnt >= int(lo) and cnt <= int(hi)


# Part 2
def is_valid_index(rule):
    """
    Returns True if password contains at least the specified
    character exactly once at either of the specified indices,
    False otherwise.

    Example: ensure char is 'r' at either index 1 or 13 exclusive
        >>> is_valid_index('1-13 r: gqdrspndrpsrjfjx')
        >>> False
    """

    p = re.compile('[-: ]+')
    i, j, c, password = p.split(rule)
    i, j = int(i) - 1, int(j) - 1
    return (password[i] == c) != (password[j] == c)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        rules = text.splitlines()

    # Solve part 1 and 2
    part1 = sum(1 for r in rules if is_valid_count(r))
    part2 = sum(1 for r in rules if is_valid_index(r))

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', part1)
    print('\nPart 2:', part2)


if __name__ == '__main__':
    main()
