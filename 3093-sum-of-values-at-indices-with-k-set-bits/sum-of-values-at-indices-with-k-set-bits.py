class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        total = 0
        for i, val in enumerate(nums):
            if bin(i).count('1') == k:
                total += val
        return total
