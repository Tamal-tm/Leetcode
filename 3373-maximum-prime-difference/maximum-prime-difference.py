class Solution(object):
    def maximumPrimeDifference(self, nums):
        checkPrime = True
        mylist=[]
        for i in range(len(nums)):
            val=nums[i] 
            for j in range(2,val):
                if val % j == 0:
                    checkPrime = False
                    break
            if checkPrime == True and val!=1:
                pos=i 
                mylist.append(pos)
            checkPrime = True
        
        if len(mylist) <= 1:
            return 0
        else:
            real_val=max(mylist)-min(mylist)
            return real_val
        