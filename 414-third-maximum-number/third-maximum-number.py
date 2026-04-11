class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))  # remove duplicates
        nums.sort(reverse=True) # sort descending
        
        if len(nums) >= 3:
            return nums[2]      # third max
        else:
            return nums[0]      # max if less than 3 unique numbers