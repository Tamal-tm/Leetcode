class Solution(object):
    def minOperations(self, nums, numsDivide):

        # ---- Helper: gcd of two numbers (no imports allowed) ----
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # ---- Step 1: find gcd of numsDivide ----
        g = numsDivide[0]
        for x in numsDivide[1:]:
            g = gcd(g, x)

        # If gcd is 1 → we only need to check smallest nums
        # Step 2: find the smallest element in nums that divides g
        nums.sort()                      

        deletions = 0
        for x in nums:
            if g % x == 0:               # x divides gcd → valid pivot
                return deletions
            deletions += 1

        # No valid number found
        return -1
