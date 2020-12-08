import sys

# Part 1
def twosum_mul(nums, target):
    """
    Returns the product of the two numbers in `nums` that
    sum up to the target, returns None if they do not exist.
    """

    seen = set()
    for n in nums:
        comp = target - n
        if comp in seen:
            return comp * n
        seen.add(n)


# Part 2
def threesum_mul(nums, target):
    """
    Returns the product of the three numbers in `nums` that
    sum up to the target, returns None if they do not exist.
    """

    for n in nums:
        sub_target = target - n
        res = twosum_mul(nums, sub_target)
        if res:
            return n * res
            

def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        nums = [int(n) for n in f.readlines()]

    # Solve part 1 and 2
    part1 = twosum_mul(nums, 2020)
    part2 = threesum_mul(nums, 2020)

    print('\nPart 1:', part1)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
