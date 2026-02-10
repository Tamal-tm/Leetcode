class Solution(object):
    def findKOr(self, nums, k):
        result=0
        for i in range(32):
            count=0
            for n in nums:
                if (n>>i) & 1:
                    count +=1
            if count >= k:
                result |= (1 << i)
        return result