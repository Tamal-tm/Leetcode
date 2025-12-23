class Solution(object):
    def findLonely(self, nums):
        nums.sort()
        mylist=[]
        if len(nums) == 1:
            return nums
        for i in range(len(nums)-1):
            next_num=nums[i]+1
            prev_num=nums[i]-1
            if next_num == nums[i+1]:
                continue
            if prev_num == nums[i-1]:
                continue
            if nums[i+1] == nums[i] or nums[i-1] == nums[i]:
                continue
            else:
                mylist.append(nums[i])
        if nums[-1] == nums[-2]:
            return mylist
        if nums[i]+1 != nums[-1]:
            mylist.append(nums[-1])
        return mylist
            
        
        