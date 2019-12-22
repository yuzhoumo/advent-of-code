import sys

def test(n):
    nums = [int(n) for n in str(n)]
    prev, adjacent = nums[0], False

    for num in nums[1:]:
        if num == prev:
            adjacent = True
        if num < prev:
            return False
        prev = num

    return True if adjacent else False


assert len(sys.argv) > 1, 'Missing argument: lower bound'
assert len(sys.argv) > 2, 'Missing argument: upper bound'
assert len(sys.argv) < 4, 'Too many arguments'

lower, upper = int(sys.argv[1]), int(sys.argv[2])
print(len([0 for n in range(lower, upper + 1) if test(n)]))
