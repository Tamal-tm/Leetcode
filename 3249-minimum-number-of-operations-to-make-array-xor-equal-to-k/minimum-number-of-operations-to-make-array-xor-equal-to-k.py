class Solution(object):
    def minOperations(self, nums, k):
        xor=0
        count=0
        for n in nums:
            xor ^=n
        val=xor ^ k
        count=bin(val).count("1")
        return count
        
