class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # If concatenations don't match, there’s no common divisor string
        if str1 + str2 != str2 + str1:
            return ""

        # Custom gcd function (no imports)
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Find GCD of string lengths
        gcd_length = find_gcd(len(str1), len(str2))
        return str1[:gcd_length]