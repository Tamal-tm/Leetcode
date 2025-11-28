class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        s = set(nums)         # unique seen numbers
        result = []

        for i in range(1, n + 1):
            if i not in s:    # if a number is not seen
                result.append(i)

        return result
