class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)
        if total % 3 == 0:
            return total

        nums.sort()  # you already sort

        # We store the smallest mod1 and mod2 elements
        mod1 = []
        mod2 = []

        for x in nums:
            if x % 3 == 1:
                mod1.append(x)
            elif x % 3 == 2:
                mod2.append(x)

        # We will try removing the minimum amount needed
        r = total % 3
        ans = 0

        # Option 1: remove 1 element with same mod
        remove1 = float('inf')
        if r == 1:
            if len(mod1) >= 1:
                remove1 = mod1[0]
        else:  # r == 2
            if len(mod2) >= 1:
                remove1 = mod2[0]

        # Option 2: remove 2 smallest from other mod group
        remove2 = float('inf')
        if r == 1:
            if len(mod2) >= 2:
                remove2 = mod2[0] + mod2[1]
        else:  # r == 2
            if len(mod1) >= 2:
                remove2 = mod1[0] + mod1[1]

        # pick the minimum removal
        best_remove = min(remove1, remove2)

        if best_remove == float('inf'):
            return 0

        return total - best_remove