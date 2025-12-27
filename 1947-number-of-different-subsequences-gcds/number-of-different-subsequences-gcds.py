class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        max_val = max(nums)
        present = [False] * (max_val + 1)

        for x in nums:
            present[x] = True

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0

        for g in range(1, max_val + 1):
            cur_gcd = 0
            for multiple in range(g, max_val + 1, g):
                if present[multiple]:
                    if cur_gcd == 0:
                        cur_gcd = multiple
                    else:
                        cur_gcd = gcd(cur_gcd, multiple)

                    if cur_gcd == g:
                        count += 1
                        break

        return count
