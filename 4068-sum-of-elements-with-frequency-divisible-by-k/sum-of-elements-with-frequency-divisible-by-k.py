class Solution(object):
    def sumDivisibleByK(self, nums, k):
        seen={}
        count=0
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for key,value in seen.items():
            if value % k == 0:
                count +=value*key
            else:
                count +=0
                
        return count