class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        sum_arr = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                sum_arr += nums[i]
        return sum_arr
