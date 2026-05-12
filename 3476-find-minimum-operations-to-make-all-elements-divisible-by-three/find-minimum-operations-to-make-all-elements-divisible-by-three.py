class Solution(object):
    def minimumOperations(self, nums):
        c=0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                c += 0
            elif nums[i] % 3 != 0:
                c += 1

        return c
            