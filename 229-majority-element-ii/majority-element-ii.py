class Solution(object):
    def majorityElement(self, nums):
        seen = {}
        mylist = []

        # frequency count
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        limit = len(nums) // 3   # threshold

        # collect elements appearing more than n/3
        for key in seen:
            if seen[key] > limit:
                mylist.append(key)

        return mylist
