import sys

# Part 1
def twosum_mul(nums, target):
    """
    Returns the product of the two numbers in `nums` that sum up to the target,
    returns None if they do not exist.
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
    Returns the product of the three numbers in `nums` that sum up to the
    target, returns None if they do not exist.
    """

    for n in nums:
        twos_target = target - n
        twos_product = twosum_mul(nums, twos_target)
        if twos_product:
            return n * twos_product


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        nums = [int(n) for n in text.splitlines()]

    # Solve part 1
    part1 = twosum_mul(nums, 2020)
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = threesum_mul(nums, 2020)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
