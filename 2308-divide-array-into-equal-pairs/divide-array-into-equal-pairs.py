class Solution(object):
    def divideArray(self, nums):
        seen={}
        div=len(nums)//2
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] +=1
            else:
                seen[nums[i]] =1
        for key, value in seen.items():
            if value % 2 == 0:
                continue
            else:
                return False
        
        return True