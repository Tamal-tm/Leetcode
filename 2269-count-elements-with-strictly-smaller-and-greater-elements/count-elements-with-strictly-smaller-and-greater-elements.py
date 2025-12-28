class Solution(object):
    def countElements(self, nums):
        nums.sort()
        smallest = nums[0]
        largest = nums[-1]

        count = 0
        for num in nums:
            if num != smallest and num != largest:
                count += 1

        return count
