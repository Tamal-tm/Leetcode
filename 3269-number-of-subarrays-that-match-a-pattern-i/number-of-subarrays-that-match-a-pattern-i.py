class Solution(object):
    def countMatchingSubarrays(self, nums, pattern):
        count = 0
        n = len(nums)
        m = len(pattern)

        # check each starting point
        for i in range(n - m):
            ok = True
            for j in range(m):
                if pattern[j] == 1 and not (nums[i+j+1] > nums[i+j]):
                    ok = False
                    break
                if pattern[j] == 0 and not (nums[i+j+1] == nums[i+j]):
                    ok = False
                    break
                if pattern[j] == -1 and not (nums[i+j+1] < nums[i+j]):
                    ok = False
                    break
            if ok:
                count += 1

        return count
