class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        new_list = []
        count = 0
        seen = set()
        
        for i in range(len(A)):
            
            if A[i] in seen:
                count += 1
            seen.add(A[i])
            
            if B[i] in seen:
                count += 1
            seen.add(B[i])
            
            new_list.append(count)
        
        return new_list
