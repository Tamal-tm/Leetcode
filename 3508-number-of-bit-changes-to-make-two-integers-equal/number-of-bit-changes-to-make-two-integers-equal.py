class Solution(object):
    def minChanges(self, n, k):
        if n == k:
            return 0
        count=0
        real_count=0
        for i in range(32):
            if n & (1<<i) > 0:
                count +=1
            if k & (1<<i) > 0:
                real_count +=1
            if n & (1<<i) == 0 and k & (1<<i) >0:
                return -1
            
        
        if count > real_count:
            return (count-real_count)
        else:
            return -1

    

        