def test(n):
    nums = [int(n) for n in str(n)]
    prev, adj = nums[0], False

    for num in nums[1:]:
        if num == prev:
            adj = True
        if num < prev:
            return False
        prev = num

    return True if adj else False

cnt = len([i for i in range(353096, 843213) if test(i)])
print(cnt)
