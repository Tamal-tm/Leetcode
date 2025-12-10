class Solution(object):
    def repeatedSubstringPattern(self, s):
        # Key trick: if s is made of repeats,
        # it will appear inside (s+s)[1:-1]
        return s in (s + s)[1:-1]
