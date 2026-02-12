class Solution(object):
    def minOperations(self, nums, k):
        xor_all = 0
        for num in nums:
            xor_all ^= num
        return bin(xor_all^k).count('1')
        
