import sys


def twosum(nums, target, seen):
    """
    Returns True if there exists two numbers in `nums` such that
    the numbers sum to `target`, False otherwise.
    """

    for n in nums:
        if target - n in seen:
            return True

    return False


# Part 1
def find_num(nums, preamble):
    """
    Returns the first number in `nums` such that no two numbers in
    the preceding `preamble` number of elements sum to it, None if
    no such number exists.
    """

    seen = set(nums[:preamble])

    for i in range(preamble, len(nums)):
        start, target = i - preamble, nums[i]
        subsequence = nums[start:i]

        if not twosum(subsequence, target, seen):
            return target

        seen.remove(subsequence[0])
        seen.add(target)


# Part 2
def longest_subseqeunce(nums, target):
    """
    Returns the longest contiguous subsequence of `nums` that sums
    to the `target` value, empty list if none exist.
    """

    sequences = []
    for window in range(2, len(nums)):
        for i in range(window - 1, len(nums) - window):
            subsequence = nums[i - window:i]
            if sum(subsequence) == target:
                sequences.append(subsequence)

    return max(sequences, key=lambda x: len(x))


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        nums = [int(n) for n in text.splitlines()]

    # Solve for parts 1 and 2
    part1 = find_num(nums, 25)
    res = longest_subseqeunce(nums, part1)
    part2 = min(res) + max(res)

    print('\nPart 1:', part1)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
