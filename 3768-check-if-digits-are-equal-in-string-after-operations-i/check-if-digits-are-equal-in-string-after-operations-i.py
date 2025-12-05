class Solution(object):
    def hasSameDigits(self, s):

        def reduce_num(x):
            x = str(x)
            while len(x) > 2:          # keep reducing until only 2 digits left
                nxt = []
                for i in range(len(x) - 1):
                    val = (int(x[i]) + int(x[i+1])) % 10
                    nxt.append(str(val))
                x = "".join(nxt)
            return x

        final = reduce_num(s)
        return final[0] == final[1]
