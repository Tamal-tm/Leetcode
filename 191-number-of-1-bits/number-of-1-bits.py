class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n = n & (n - 1)   # removes the rightmost set bit
            count += 1
        return count
