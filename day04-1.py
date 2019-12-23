import sys


def test(n):
    prev, n, adjacent = n % 10, n // 10, False

    while n:
        d = n % 10
        if d > prev:
            return False
        if d == prev:
            adjacent = True
        prev, n = d, n // 10

    return adjacent


def count(lower, upper):
    cnt = 0
    for n in range(lower, upper):
        if test(n):
            cnt += 1
    return cnt


assert len(sys.argv) > 1, 'Missing argument: lower bound'
assert len(sys.argv) > 2, 'Missing argument: upper bound'
assert len(sys.argv) < 4, 'Too many arguments'

print(count(int(sys.argv[1]), int(sys.argv[2])))
