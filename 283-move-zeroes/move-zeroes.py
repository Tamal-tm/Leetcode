class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                nums.append(0)
                nums[i] = None  # mark removed zeros safely

        new_list = []
        for num in nums:
            if num is not None:
                new_list.append(num)

        # Step 3: Copy back into nums (in-place update)
        nums[:] = new_list
        return nums