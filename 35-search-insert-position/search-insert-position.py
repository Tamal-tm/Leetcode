class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # find middle index
            
            if nums[mid] == target:
                return mid              # target found
            elif nums[mid] < target:
                left = mid + 1          # search in right half
            else:
                right = mid - 1         # search in left half
        
        return left  # target not found → insertion position
