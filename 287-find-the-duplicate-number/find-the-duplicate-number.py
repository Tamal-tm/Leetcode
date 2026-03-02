class Solution(object):
    def findDuplicate(self, nums):
        seen={}
        c=1
        for i in range(len(nums)):
            a=nums[i]
            if a in seen:
                c +=1
                return a
            else:
                seen[a] = c
            c=0