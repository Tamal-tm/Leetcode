class Solution(object):
    def firstMissingPositive(self, nums):
        nums = set([x for x in nums if x > 0])  # keep only positive unique numbers
        i = 1
        while i in nums:
            i += 1
        return i
