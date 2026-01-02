class Solution(object):
    def maximumCount(self, nums):
        n=p=0
        for i in nums:
            if i<0:
                n+=1
            elif i>0:
                p+=1
        return max(n,p)
