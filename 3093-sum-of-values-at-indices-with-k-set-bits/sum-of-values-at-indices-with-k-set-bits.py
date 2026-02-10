class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        total = 0
        for i, val in enumerate(nums):
            bin_idx = bin(i)
            if bin_idx.count('1') == k:
                total += val
        return total
