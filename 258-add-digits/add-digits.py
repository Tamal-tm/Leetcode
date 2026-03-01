class Solution(object):
    def addDigits(self, num):
        while num >= 10:  # repeat until single-digit
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num