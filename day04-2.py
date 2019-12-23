import sys


def test(n, adj):
    prev, n, adjacent = n % 10, n // 10, adj

    while n:
        d = n % 10
        if d > prev:
            return False
        if d == prev:
            adjacent[d] += 1
        prev, n = d, n // 10

    if 2 in adjacent:
        return True
    return False


def count(lower, upper):
    cnt, adj = 0, [1 for i in range(0, 10)]
    for n in range(lower, upper):
        if test(n, list(adj)):
            cnt += 1
    return cnt


assert len(sys.argv) > 1, 'Missing argument: lower bound'
assert len(sys.argv) > 2, 'Missing argument: upper bound'
assert len(sys.argv) < 4, 'Too many arguments'

print(count(int(sys.argv[1]), int(sys.argv[2])))

