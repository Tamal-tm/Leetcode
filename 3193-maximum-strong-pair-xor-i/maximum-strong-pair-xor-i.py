class Solution(object):
    def maximumStrongPairXor(self, nums):
        nums.sort()
        max_xor = 0
        n = len(nums)

        for i in range(n):
            j = i
            while j < n and nums[j] <= 2 * nums[i]:
                max_xor = max(max_xor, nums[i] ^ nums[j])
                j += 1
        return max_xor
