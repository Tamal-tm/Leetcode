class Solution(object):
    def hasTrailingZeros(self, nums):
        even_count = 0
        for n in nums:
            if n & 1 == 0:
                even_count += 1
            if even_count == 2:
                return True
        return False
