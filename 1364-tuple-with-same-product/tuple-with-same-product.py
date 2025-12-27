class Solution(object):
    def tupleSameProduct(self, nums):
        from collections import defaultdict

        prod_count = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                prod_count[prod] += 1

        count = 0
        for k in prod_count.values():
            if k > 1:
                count += k * (k - 1) * 4

        return count
