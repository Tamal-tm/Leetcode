class Solution(object):
    def totalHammingDistance(self, nums):
        n = len(nums)
        total = 0
        
        for bit in range(32):
            ones = 0
            mask = 1 << bit
            
            for num in nums:
                if num & mask:
                    ones += 1
            
            total += ones * (n - ones)
        return total
