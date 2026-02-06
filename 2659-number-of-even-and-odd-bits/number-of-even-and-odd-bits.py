class Solution(object):
    def evenOddBit(self, n):
        even_count = 0
        odd_count = 0

        for i in range(16):
            if n & (1 << i):
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

        return [even_count, odd_count]
