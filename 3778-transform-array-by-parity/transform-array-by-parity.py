class Solution(object):
    def transformArray(self, nums):
        mylist=[]
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                mylist.append(0)
        
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                mylist.append(1)
        
        return mylist