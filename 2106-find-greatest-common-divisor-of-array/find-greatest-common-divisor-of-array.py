class Solution(object):
    def findGCD(self, nums):
        def gcd(l, m):
            if l==0:
              return m
            return gcd(m%l, l)
        return gcd(min(nums), max(nums))