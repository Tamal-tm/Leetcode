class Solution(object):
    def intersection(self, nums):
        common = set(nums[0])
        for arr in nums[1:]:
            common &= set(arr)
        return sorted(common)
