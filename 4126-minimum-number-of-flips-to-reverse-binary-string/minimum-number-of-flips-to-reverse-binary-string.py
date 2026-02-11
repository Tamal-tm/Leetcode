class Solution(object):
    def minimumFlips(self, n):
        s = bin(n)[2:]
        r = s[::-1]
        
        flips = 0
        for i in range(len(s)):
            if s[i] != r[i]:
                flips += 1
        
        return flips
