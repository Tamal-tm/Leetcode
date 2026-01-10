class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        count = 0

        for i in range(n):
            target_count = 0
            other_count = 0

            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                else:
                    other_count += 1

                if target_count > other_count:
                    count += 1

        return count
