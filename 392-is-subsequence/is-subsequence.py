class Solution(object):
    def isSubsequence(self, s, t):
        j = 0
        for ch in t:
            if j < len(s) and s[j] == ch:
                j += 1
        return j == len(s)