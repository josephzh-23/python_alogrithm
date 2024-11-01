def answer(nums):
    s = []
    n = len(nums)
    ans = [0] * len(nums)

    s.append(nums[len(nums) - 1])
    ans[n - 1] = -1
    for i in range(n - 2, 0, -1):
        ans[i] = s[-1]
        if s[-1] < nums[i]:
            s.append(nums[i])
    print(ans)
    return ans


nums = [17, 18, 5, 4, 6, 1]
answer(nums)
