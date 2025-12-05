class Solution(object):
    def hasSameDigits(self, s):

        def repeat(x):
            x = list(map(int, str(x)))        # convert to list of digits
            while len(x) > 2:                 # keep reducing until 2 digits remain
                nxt = []
                for i in range(len(x) - 1):
                    nxt.append((x[i] + x[i+1]) % 10)
                x = nxt
            return x

        res = repeat(s)
        return res[0] == res[1]
