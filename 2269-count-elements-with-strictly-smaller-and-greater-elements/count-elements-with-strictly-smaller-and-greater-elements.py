class Solution(object):
    def countElements(self, nums):
        nums.sort()
        val_1=nums[0]
        val_2=nums[-1]
        filtered_list = [item for item in nums if item != val_1]
        filtered_list = [item for item in filtered_list if item != val_2]
        val=len(filtered_list)
        return val
        