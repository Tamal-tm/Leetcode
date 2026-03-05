class Solution(object):
    def solve(self, index, target, subset, nums, result):

        if target == 0:
            result.append(subset[:])
            return

        if index >= len(nums):
            return

        if nums[index] <= target:
            subset.append(nums[index])
            self.solve(index, target - nums[index], subset, nums, result)
            subset.pop()

        self.solve(index + 1, target, subset, nums, result)


    def combinationSum(self, candidates, target):
        result = []
        self.solve(0, target, [], candidates, result)
        return result