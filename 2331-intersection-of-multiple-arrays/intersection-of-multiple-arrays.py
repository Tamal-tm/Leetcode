class Solution(object):
    def intersection(self, nums):
        seen = {}

        # Count elements of first array
        for i in range(len(nums[0])):
            if nums[0][i] in seen:
                seen[nums[0][i]] += 1
            else:
                seen[nums[0][i]] = 1

        # Check against remaining arrays
        for j in range(1, len(nums)):
            current_set = set(nums[j])
            for key in list(seen.keys()):
                if key not in current_set:
                    del seen[key]

        return sorted(list(seen.keys()))