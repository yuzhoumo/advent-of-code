import aoc
from collections import defaultdict

def blink(nums):
    res = []
    for n in nums:
        if n == 0:
            res.append(1)
        elif (len(str(n)) % 2) == 0:
            sn = str(n)
            res.append(int(sn[:len(sn)//2]))
            res.append(int(sn[len(sn)//2:]))
        else:
            res.append(n * 2024)
    return res


def blink2(nums):
    res = defaultdict(int)
    for n in nums.keys():
        if n == 0:
            res[1] += nums[0]
        elif (len(str(n)) % 2) == 0:
            sn = str(n)
            res[int(sn[:len(sn)//2])] += nums[n]
            res[int(sn[len(sn)//2:])] += nums[n]
        else:
            res[n * 2024] += nums[n]
    return res


def part1(nums):
    res = nums
    for _ in range(25):
        res = blink(res)
    return len(res)


def part2(nums):
    stones = defaultdict(int)
    for n in nums:
        stones[n] += 1

    for _ in range(75):
        stones = blink2(stones)

    return sum(stones.values())


def main(text):
    data = text.strip()
    nums = [int(n) for n in data.split()]
    return part1(nums), part2(nums)


if __name__ == "__main__":
    aoc.run(main, 11)
