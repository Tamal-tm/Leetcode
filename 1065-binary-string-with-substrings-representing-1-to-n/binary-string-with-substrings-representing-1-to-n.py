class Solution(object):
    def queryString(self, s, n):
        
        if n > len(s) * 2:
            return False
        
        for i in range(1, n + 1):
            
            # skip unnecessary small values
            if i <= n // 2:
                continue
            
            bin_val = bin(i)[2:]
            
            if bin_val not in s:
                return False
        
        return True
