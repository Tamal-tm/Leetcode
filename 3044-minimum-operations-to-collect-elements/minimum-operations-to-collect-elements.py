class Solution(object):
    def minOperations(self, nums, k):
        seen = set()
        ops = 0

        for i in range(len(nums) - 1, -1, -1):
            ops += 1
            if nums[i] <= k:
                seen.add(nums[i])
            if len(seen) == k:
                return ops
