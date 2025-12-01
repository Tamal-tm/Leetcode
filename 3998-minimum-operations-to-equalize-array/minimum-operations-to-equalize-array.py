class Solution(object):
    def minOperations(self, nums):
        n = len(nums)

        # Case 0: all elements already equal
        if min(nums) == max(nums):
            return 0

        # Compute final AND
        final_value = nums[0]
        for x in nums:
            final_value &= x

        # Case: if final value == all elements
        if all(x == final_value for x in nums):
            return 0

        # Case 1: check if ANY element is already equal to final AND
        # or ANY subarray's AND equals final_value
        for i in range(n):
            current = nums[i]
            if current == final_value:
                return 1
            for j in range(i+1, n):
                current &= nums[j]
                if current == final_value:
                    return 1

        # Otherwise needs 2 operations
        return 2
