class Solution(object):
    def maxAdjacentDistance(self, nums):
        length = len(nums)
        max_diff = 0
        
        for i in range(length):
            diff = abs(nums[i] - nums[(i + 1) % length])
            if diff > max_diff:
                max_diff = diff
                
        return max_diff