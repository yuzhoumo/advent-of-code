import sys
from functools import reduce

# Part 1
def earliest_product(timestamp, bus_ids):
    """
    Finds the id of the earliest bus given an arrival timestamp of the
    passenger and a list of bus ids. Returns the product of the earliest bus
    id and wait time for that bus.
    """

    earliest = wait_time = sys.maxsize

    for i in bus_ids:
        tmp = i - (timestamp % i)
        if tmp < wait_time:
            earliest = i
            wait_time = tmp

    return earliest * wait_time


# Part 2
def crt(n, r):
    """
    Chinese Remainder Theorem: Find a solution to the system of modular
    equations given that the elements of `n` are relatively prime.

    Example:
        >>> crt([5, 7], [1, 3])
        31

    Explanation:
        x = 1 mod 5
        x = 3 mod 7
        x = 31 is the smallest number s.t. 31 % 5 = 1 and 31 % 7 = 3
    """

    def egcd(a, b):  # Extended Euclidian algorithm
        if b == 0: return (1, 0)
        c, d = egcd(b, a % b)
        return d, c - a // b * d

    def inverse_mod(r, n):  # Inverse modulo
        a = egcd(r, n)[0]
        if a < 0: a = (a % n + n) % n
        return a

    product, total = reduce(lambda a, b: a * b, n), 0
    for nth, rth in zip(n, r):
        p = product // nth
        total += rth * inverse_mod(p, nth) * p
    return total % product


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        timestamp = int(f.readline().strip())
        schedule = f.readline().strip().split(',')

    # Parse input
    bus_ids, remainders = [], []
    for i, n in enumerate(schedule):
        if n.isnumeric():
            bus_id = int(n)
            bus_ids.append(bus_id)
            remainders.append(-i % bus_id)

    # Solve part 1
    part1 = earliest_product(timestamp, bus_ids)
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = crt(bus_ids, remainders)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
