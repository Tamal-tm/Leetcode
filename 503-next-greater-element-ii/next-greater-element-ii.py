class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n    # Initialize results with -1
        stack = []           # Stack for potential NGEs

        # Loop twice to simulate circular array
        for i in range(2 * n - 1, -1, -1):
            # Maintain decreasing stack
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            # Only set result during the first 'real' pass
            if i < n:
                if stack:
                    result[i] = stack[-1]
            # Push current value for next iteration checks
            stack.append(nums[i % n])
        return result