class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        op = 0
        max_op = float('-inf')

        for i in range(len(nums)):
            op += nums[i]
            max_op = max(max_op, op)

            if op < 0:
                op = 0

        return max_op
