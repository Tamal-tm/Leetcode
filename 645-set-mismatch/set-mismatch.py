class Solution(object):
    def findErrorNums(self, nums):
        seen = {}
        mylist = []
        duplicate = missing = None

        # Count each number only once
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen[num] = 1

        # Find missing using set difference
        n = len(nums)
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]