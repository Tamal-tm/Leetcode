class Solution(object):
    def countDistinctIntegers(self, nums):
        n=len(nums)
        for i in range(n):
            s=str(nums[i])
            if len(s)>1:
                rev=s[::-1]
                nums.append(int(rev))
        nums=set(nums)
        return len(nums)
