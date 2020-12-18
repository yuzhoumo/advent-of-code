import sys
import re


# Part 1
def is_valid_count(rule):
    """
    Returns True if password contains at least the minimum and at most the
    maximum of a specified character, False otherwise.

    Example: ensure password contains between 1-13 'r' chars
        >>> is_valid_count('1-13 r: gqdrspndrpsrjfjx')
        True
    """

    pattern = re.compile('[-: ]+')
    lo, hi, character, password = pattern.split(rule)
    count = password.count(character)
    return count >= int(lo) and count <= int(hi)


# Part 2
def is_valid_index(rule):
    """
    Returns True if password contains at least the specified character exactly
    once at either of the specified indices, False otherwise.

    Example: ensure char is 'r' at either index 1 or 13 exclusive
        >>> is_valid_index('1-13 r: gqdrspndrpsrjfjx')
        False
    """

    pattern = re.compile('[-: ]+')
    i, j, character, password = pattern.split(rule)
    i, j = int(i) - 1, int(j) - 1
    return (password[i] == character) != (password[j] == character)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        rules = text.splitlines()

    # Solve part 1
    part1 = sum(1 for r in rules if is_valid_count(r))
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = sum(1 for r in rules if is_valid_index(r))
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
