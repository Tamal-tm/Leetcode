class Solution(object):
    def divideArray(self, nums):
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for count in seen.values():
            if count % 2 != 0:
                return False

        return True
