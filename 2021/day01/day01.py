import sys

# Part 1
def num_increasing(nums):
    """
    Returns the number of times the ith number in a sequence is
    greater than the number before it.
    """
    if len(nums) < 2: return 0
    return sum(nums[i] > nums[i-1] for i in range(1, len(nums)))


# Part 2
def num_increasing_sums(nums):
    """
    Returns the number of times the ith sliding window sum of 3
    numbers in a sqequence is greater than the sum before it.
    """
    if len(nums) < 4: return 0
    sums = [sum(nums[i:i+3]) for i in range(len(nums) - 2)]
    return num_increasing(sums)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        nums = [int(n) for n in f.read().splitlines()]

    # Solve part 1
    part1 = num_increasing(nums)
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = num_increasing_sums(nums)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
