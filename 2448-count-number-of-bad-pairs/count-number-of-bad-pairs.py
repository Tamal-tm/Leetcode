class Solution(object):
    def countBadPairs(self, nums):
        seen = {}
        good = 0
        n = len(nums)

        for i in range(n):
            key = nums[i] - i
            if key in seen:
                good += seen[key]
                seen[key] += 1
            else:
                seen[key] = 1

        total = n * (n - 1) // 2
        return total - good
