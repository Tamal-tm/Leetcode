class Solution(object):
    def minOperations(self, nums, k):
        diff=0
        count=0
        new_diff=None
        max_num=sum(nums)
        if sum(nums) == k:
            return 0 
        if sum(nums) < k:
            return sum(nums)
        if sum(nums) > k:
            for i in range(len(nums)):
                if len(nums)>1:
                    diff=sum(nums)-nums[i]
                    if new_diff is None or diff > new_diff:
                        new_diff=diff
                else:
                    new_diff=sum(nums)
        
        for j in range(1,new_diff):
            
            if max_num % k == 0:
                return count
            else:
                max_num -=1
                count +=1
        
        return count