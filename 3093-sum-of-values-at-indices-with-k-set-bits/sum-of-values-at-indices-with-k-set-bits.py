class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        sum_arr=0
        for i in range(len(nums)):
            count=0
            for j in range(0,16):
                if i & (1<<j) > 0:
                    count +=1
            if count == k:
                sum_arr +=nums[i]
        
        return sum_arr

        