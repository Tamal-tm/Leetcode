class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] <= nums[high]:
                high = mid       # minimum is at mid or left
            else:
                low = mid + 1    # minimum is on right side
        
        return nums[low]
