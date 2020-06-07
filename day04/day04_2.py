import sys

""" Day 4: Secure Container (Part 2)

An Elf just remembered one more important detail: the two adjacent
matching digits are not part of a larger group of matching digits. Given
this additional criterion, but still ignoring the range rule, the
following are now true:

- 112233 meets these criteria because the digits never decrease and all
  repeated digits are exactly two digits long.
- 123444 no longer meets the criteria (the repeated 44 is part of a
  larger group of 444).
- 111122 meets the criteria (even though 1 is repeated more than twice,
  it still contains a double 22).

How many different passwords within the range given in your puzzle input
meet all of the criteria? """


def is_valid_password(n, adj_counts):
    prev, n, adjacent = n % 10, n // 10, adj_counts

    while n:  # Parses number right to left
        d = n % 10
        if d > prev:
            return False
        if d == prev:
            # Keeps track how many same adjacent values for each digit
            adjacent[d] += 1
        prev, n = d, n // 10

    # Is valid if passes above and any digit has exactly 1 identical
    # adjacent value
    return 1 in adjacent


def count(lower, upper):
    cnt, adj_counts = 0, tuple(0 for i in range(0, 10))
    for n in range(lower, upper):
        # adj_counts tracks number of same adj values for each digit
        if is_valid_password(n, list(adj_counts)):
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
