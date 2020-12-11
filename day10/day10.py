import sys
from collections import defaultdict


# Part 1
def ones_threes_product(sorted_nums):

    # prev = 0 (wall jolts), threes = 1 (device jolts)
    prev, ones, threes = 0, 0, 1

    for n in sorted_nums:
        diff = n - prev
        if diff == 3:
            threes += 1
        elif diff == 1:
            ones += 1
        prev = n
    
    return ones * threes


# Part 2
def num_arrangements(sorted_nums):

    counts = defaultdict(int)
    counts[0] = 1

    for n in sorted_nums:
        counts[n] += counts[n-1] + counts[n-2] + counts[n-3]

    return counts[sorted_nums[-1]]


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        nums = [int(n) for n in text.splitlines()]

    # Solve for parts 1 and 2
    nums.sort()
    part1 = ones_threes_product(nums)
    part2 = num_arrangements(nums)

    print('\nPart 1:', part1)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
