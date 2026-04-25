class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums.count(1) == 0: return True
        start = nums.index(1)
        counter = 0
        for i in range(start+1,len(nums)):
            if nums[i] == 0:
                counter += 1
            else:
                if counter >= k:
                    counter = 0
                else:
                    return False
        return True