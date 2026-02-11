class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        
        for p in nums:
            # if p is even, impossible (OR of consecutive numbers is always odd)
            if p % 2 == 0:
                ans.append(-1)
                continue
            
            # find position of rightmost zero in p
            x = 0
            while (p >> x) & 1:
                x += 1
            
            # smallest answer
            ans.append(p - (1 << (x - 1)))
        
        return ans

