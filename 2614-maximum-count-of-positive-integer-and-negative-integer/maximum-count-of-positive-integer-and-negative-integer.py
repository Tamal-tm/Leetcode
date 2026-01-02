class Solution(object):
    def maximumCount(self, nums):
        count_pos=0
        count_neg=0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] >= 1:
                count_pos +=1 
            if nums[i] <= -1:
                count_neg +=1
        return max(count_neg,count_pos)