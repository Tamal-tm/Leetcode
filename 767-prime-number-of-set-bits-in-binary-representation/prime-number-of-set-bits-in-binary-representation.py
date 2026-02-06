class Solution(object):
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0

        for i in range(left, right + 1):
            count = 0
            n = i
            while n:
                n &= (n - 1)   # removes lowest set bit
                count += 1

            if count in primes:
                ans += 1

        return ans
