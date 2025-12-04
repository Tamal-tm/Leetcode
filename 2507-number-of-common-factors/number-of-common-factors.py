class Solution(object):
    def commonFactors(self, a, b):
        def gcd(a, b):
            if a > b:
                return gcd(b, a)

            count = 0
            i = 1
            while i * i <= a:        # loop only till sqrt(a)
                if a % i == 0:
                    if b % i == 0:
                        count += 1
                    j = a // i       # paired factor
                    if j != i and b % j == 0:
                        count += 1
                i += 1
            return count

        return gcd(a, b)
