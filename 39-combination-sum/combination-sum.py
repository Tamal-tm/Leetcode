class Solution(object):

    def solve(self, index, total, subset, nums, target, result):

        if total == target:
            result.append(subset[:])
            return

        if total > target:
            return

        if index >= len(nums):
            return

        # PICK
        subset.append(nums[index])
        Sum = total + nums[index]
        self.solve(index, Sum, subset, nums, target, result)

        # BACKTRACK
        subset.pop()

        # NOT PICK
        self.solve(index + 1, total, subset, nums, target, result)
    def combinationSum(self, candidates, target):
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result