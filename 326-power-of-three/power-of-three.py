class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            while n != 1:
                n = n // 3
                if n % 3 == 0:
                    continue
                elif n == 1:
                    return True
                else:
                    return False
        else:
            return False
        return True
