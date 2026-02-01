class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        tot_subsets=1<<n
        result=[]
        for num in range(0,tot_subsets):
            mylist=[]
            for i in range(0,n):
                if num & (1<<i)!=0:
                    mylist.append(nums[i])
            result.append(mylist)
        return result