class Solution(object):
    def tupleSameProduct(self, nums):
        seen = {}
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]

                if prod in seen:
                    count += 8 * seen[prod]
                    seen[prod] += 1
                else:
                    seen[prod] = 1

        return count
