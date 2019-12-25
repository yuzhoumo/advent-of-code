import sys

""" Day 4: Secure Container (Part 1)

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on
a sticky note, but someone threw it out. However, they do remember a few key facts about the password:

- It is a six-digit number.
- The value is within the range given in your puzzle input.
- Two adjacent digits are the same (like 22 in 122345).
- Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

How many different passwords within the range given in your puzzle input meet these criteria? """


def is_valid_password(n):
    prev, n, adjacent = n % 10, n // 10, False

    while n:  # Parses number right to left
        d = n % 10
        if d > prev:
            return False
        if d == prev:
            adjacent = True
        prev, n = d, n // 10

    return adjacent  # Is valid if non-decreasing check doesn't fail and adjacent is True


def count(lower, upper):
    cnt = 0
    for n in range(lower, upper):
        if is_valid_password(n):
            cnt += 1
    return cnt


def main():
    assert len(sys.argv) > 1, 'Missing argument: lower bound'
    assert len(sys.argv) > 2, 'Missing argument: upper bound'
    assert len(sys.argv) < 4, 'Too many arguments'
    lower_bound, upper_bound = int(sys.argv[1]), int(sys.argv[2])

    print(count(lower_bound, upper_bound))


if __name__ == '__main__':
    main()
