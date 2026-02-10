class Solution(object):
    def hasTrailingZeros(self, nums):
        orr=0
        if len(nums) == 1:
            return nums[1] & 1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                orr = nums[i] | nums[j] 
                if orr & 1 == 0:
                    return True
        return False
        