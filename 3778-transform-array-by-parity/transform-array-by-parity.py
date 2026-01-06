class Solution(object):
    def transformArray(self, nums):
        zeros = 0
        ones = 0

        for n in nums:
            if n % 2 == 0:
                zeros += 1
            else:
                ones += 1

        return [0] * zeros + [1] * ones
