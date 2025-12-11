class Solution(object):
    def longestPrefix(self, s):
        mod = 10**9 + 7
        base = 31
        
        prefix_hash = 0
        suffix_hash = 0
        power = 1
        
        n = len(s)
        res_len = 0
        
        # check all prefix lengths from 1 to n-1
        for i in range(n - 1):
            # prefix grows left→right
            prefix_hash = (prefix_hash * base + (ord(s[i]) - 96)) % mod
            
            # suffix grows right→left
            suffix_hash = (suffix_hash + (ord(s[n-1-i]) - 96) * power) % mod
            
            power = (power * base) % mod
            
            if prefix_hash == suffix_hash:
                res_len = i + 1   # longest so far
        
        return s[:res_len]
