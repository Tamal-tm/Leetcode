class Solution(object):
    def minLengthAfterRemovals(self, s):
        if len(set(s)) == 1:
            return len(s)

        c1 = s.count(s[0])
        c2 = len(s) - c1

        return abs(c1 - c2)
