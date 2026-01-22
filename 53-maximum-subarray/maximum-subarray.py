class Solution(object):
    def maxSubArray(self, nums):
        op = nums[0]
        max_op = nums[0]

        for i in range(1, len(nums)):
            if op < 0:
                op = nums[i]
            else:
                op += nums[i]

            if op > max_op:
                max_op = op

        return max_op
