def test(n):
    nums = [int(n) for n in str(n)]
    prev, adj = nums[0], {i:1 for i in range(0, 10)}

    for num in nums[1:]:
        if num < prev:
            return False
        if num == prev:
            adj[num] += 1
        prev = num

    for n in adj.values():
        if n == 2:
            return True
    return False

cnt = len([i for i in range(353096, 843213) if test(i)])
print(cnt)
