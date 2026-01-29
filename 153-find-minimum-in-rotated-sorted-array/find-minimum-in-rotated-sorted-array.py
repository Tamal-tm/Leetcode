class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1
        min_val= float ("inf")

        while low<=high:
            mid=(low+high)//2
            if nums[mid] < min_val:
                min_val=nums[mid]
            if nums[mid]<=nums[high]:
                min_val=min(min_val,nums[mid])
                high=mid-1 # We will go opposite
            else:
                min_val=min(min_val,nums[low])
                low=mid+1
            
        return min_val

        