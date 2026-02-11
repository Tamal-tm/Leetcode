class Solution(object):
    def countMonobit(self, n):
        count = 0
        
        k = 0
        while True:
            val = (1 << k) - 1
            if val > n:
                break
            count += 1
            k += 1
        
        return count
