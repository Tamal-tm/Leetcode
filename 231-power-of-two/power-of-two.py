class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        total = 1
        while total < n:
            total = total * 2
        return total == n
