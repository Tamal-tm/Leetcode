class Solution(object):
    def sumDivisibleByK(self, nums, k):
        seen={}
        count=0
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] +=1
            else:
                seen[nums[i]] =1
        
        for key,value in seen.items():
            if value % k == 0:
                count +=value*key
            else:
                count +=0
                
        return count