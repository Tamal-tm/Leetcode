class Solution(object):
    def canConstruct(self, s, k):
        if k > len(s):
            return False
        
        seen = {}
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        
        odd = 0
        for val in seen.values():
            if val % 2 == 1:
                odd += 1
        
        return odd <= k
