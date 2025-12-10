class Solution(object):
    def repeatedStringMatch(self, a, b):
        base = len(b) // len(a)

        for x in (base, base+1, base+2):
            if b in a * x:
                return x
        return -1
