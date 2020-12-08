import sys

# Part 1
def twosum_mul(nums, target):
    seen = set()
    for n in nums:
        comp = target - n
        if comp in seen:
            return comp * n
        seen.add(n)


# Part 2
def threesum_mul(nums, target):
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

    print('\nInput:', nums)
    print('\nPart 1:', twosum_mul(nums, 2020))
    print('\nPart 2:', threesum_mul(nums, 2020))


if __name__ == '__main__':
    main()
