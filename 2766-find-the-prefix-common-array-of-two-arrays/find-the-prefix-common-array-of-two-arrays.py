class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        new_list = []
        count = 0
        n = len(A)
        seen = [0] * (n + 1)
        
        for i in range(n):
            
            seen[A[i]] += 1
            if seen[A[i]] == 2:
                count += 1
            
            seen[B[i]] += 1
            if seen[B[i]] == 2:
                count += 1
            
            new_list.append(count)
        
        return new_list
