class Solution(object):
    def findKOr(self, nums, k):
        result = 0
        for i in range(32):
            bit = 1 << i
            count = 0
            for n in nums:
                if n & bit:
                    count += 1
                    if count == k:
                        result |= bit
                        break
        return result
