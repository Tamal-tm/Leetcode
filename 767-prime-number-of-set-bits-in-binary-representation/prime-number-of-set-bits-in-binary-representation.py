class Solution(object):
    def countPrimeSetBits(self, left, right):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        real_count = 0

        for i in range(left, right + 1):
            count = 0
            for j in range(20):
                if i & (1 << j):
                    count += 1

            if count in primes:
                real_count += 1

        return real_count
