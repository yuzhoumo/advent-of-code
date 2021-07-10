import sys
import re


# Part 1 & 2
def number_game(nums, nth):
    seen = { n : i for i, n in enumerate(nums[:-1]) }

    prev = nums[-1]
    for i in range(len(nums), nth):
        curr = 0 if prev not in seen else (i - 1) - seen[prev]
        seen[prev] = i - 1
        prev = curr

    return curr


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        nums = [int(n) for n in f.read().split(',')]

    # Solve part 1
    part1 = number_game(nums, 2020)
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = number_game(nums, 30000000)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
