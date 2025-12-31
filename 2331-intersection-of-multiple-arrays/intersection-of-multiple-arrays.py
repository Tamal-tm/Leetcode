class Solution(object):
    def intersection(self, nums):
        seen = {}

        # Count elements of the first array
        for x in nums[0]:
            seen[x] = seen.get(x, 0) + 1

        # Process remaining arrays
        for i in range(1, len(nums)):
            current = {}
            for x in nums[i]:
                if x in seen:
                    current[x] = 1
            seen = current  # keep only common elements

        return sorted(seen.keys())
