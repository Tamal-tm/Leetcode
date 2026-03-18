class Solution(object):
    def countDigitOne(self, n):
        c = 0
        i = 1  # start from ones place

        while i <= n:
            left = n // (i * 10)
            curr = (n // i) % 10
            right = n % i

            if curr == 0:
                c += left * i
            elif curr == 1:
                c += left * i + right + 1
            else:
                c += (left + 1) * i

            i = i * 10  # move to next digit place

        return c