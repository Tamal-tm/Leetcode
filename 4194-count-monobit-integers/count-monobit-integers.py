class Solution(object):
    def countMonobit(self, n):
        current = 0
        power = 0
       
        while current <= n:
            current += 2**power
            power += 1
            
        return power