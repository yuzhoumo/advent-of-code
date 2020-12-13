import sys


# Part 1
def twosum(nums, target, seen):
    """
    Returns True if there exists two numbers in `nums` such that the numbers sum
    to `target`, False otherwise.
    """

    for n in nums:
        if target - n in seen:
            return True

    return False


def find_num(nums, preamble):
    """
    Returns the first number in `nums` such that no two numbers in the preceding
    `preamble` number of elements sum to it, None if no such number exists.
    """

    seen = set(nums[:preamble])

    for i in range(preamble, len(nums)):
        start, target = i - preamble, nums[i]
        subsequence = nums[start : i]

        if not twosum(subsequence, target, seen):
            return target

        seen.remove(subsequence[0])
        seen.add(target)


# Part 2
def longest_subseq_minmax_sum(nums, target):
    """
    Returns the longest contiguous subsequence of `nums` that sums to the
    `target` value, empty list if none exist.
    """

    # Create cumulative sums to enable O(1) range sum queries
    prefix_sums = [0]
    for n in nums:
        prefix_sums.append(prefix_sums[-1] + n)

    for window in range(2, len(nums)):
        for i in range(len(nums) - window):

            # Get sum of the subsequence
            range_sum = prefix_sums[i + window] - prefix_sums[i]

            if range_sum == target:
                subsequence = nums[i : i + window]
                return min(subsequence) + max(subsequence)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        nums = [int(n) for n in text.splitlines()]

    # Solve part 1
    part1 = find_num(nums, 25)
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = longest_subseq_minmax_sum(nums, part1)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
