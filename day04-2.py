import sys

def test(n):
    nums = [int(n) for n in str(n)]
    prev, adjacent = nums[0], {i: 1 for i in range(0, 10)}

    for num in nums[1:]:
        if num < prev:
            return False
        if num == prev:
            adjacent[num] += 1
        prev = num

    for n in adjacent.values():
        if n == 2:
            return True
    return False


assert len(sys.argv) > 1, 'Missing argument: lower bound'
assert len(sys.argv) > 2, 'Missing argument: upper bound'
assert len(sys.argv) < 4, 'Too many arguments'

lower, upper = int(sys.argv[1]), int(sys.argv[2])
print(len([0 for n in range(lower, upper + 1) if test(n)]))
