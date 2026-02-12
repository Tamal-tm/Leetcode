class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        result = []
        freq = [0] * (n + 1)
        count = 0
        
        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                count += 1
                
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                count += 1
                
            result.append(count)
            
        return result
