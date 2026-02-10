class Solution(object):
    def maximumStrongPairXor(self, nums):
        max_xor=0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i],nums[j]):
                    xor=nums[i]^nums[j]
                    max_xor=max(max_xor,xor)
        
        return max_xor
        