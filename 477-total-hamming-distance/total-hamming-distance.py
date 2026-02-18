class Solution(object):
    def totalHammingDistance(self, nums):
        count = 0
        n = len(nums)
        
        for bit in range(32):
            ones = 0
            
            for i in range(n):
                if nums[i] & (1 << bit):
                    ones += 1
            
            count += ones * (n - ones)
        
        return count
