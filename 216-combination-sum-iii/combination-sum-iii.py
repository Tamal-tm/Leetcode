class Solution(object):
    def combinationSum3(self, k, n):
        from itertools import combinations
        
        result = []
        nums = [1,2,3,4,5,6,7,8,9]

        # Try every combination of size k
        for combo in combinations(nums, k):
            if sum(combo) == n:
                result.append(list(combo))

        return result
