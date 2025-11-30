class Solution(object):
    def minSubarray(self, nums, p):
        total = sum(nums)
        mod = total % p

        # If already divisible → no removal needed
        if mod == 0:
            return 0

        prefix = 0
        seen = {0: -1}     # prefix_sum % p → index
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            # We want:
            # (prefix - target) % p = needed prefix in the past
            target = (prefix - mod) % p

            if target in seen:
                res = min(res, i - seen[target])

            seen[prefix] = i

        return res if res < len(nums) else -1
