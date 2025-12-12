class Solution(object):
    def majorityElement(self, nums):
        seen={}
        mylist=[]
        if len(nums) == 2 and nums[0]!=nums[1]:
            return nums
        elif len(nums)<3:
            mylist.append(nums[0])
            return mylist
        else:
            val=(len(nums)/3)
            for i in range(len(nums)):
                if nums[i] in seen:
                    seen[nums[i]] +=1
                else:
                    seen[nums[i]] = 1

            for ch in seen:
                if seen[ch]>val:
                    mylist.append(ch)
                
        return mylist