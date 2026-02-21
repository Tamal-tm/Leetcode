class Solution(object):
    def singleNumber(self, nums):
        freq={}
        for x in nums:
            if x in freq:
                freq[x] +=1
            else:
                freq[x] =1
                m=freq[x]
        
        for x in freq:
            if freq[x] == 1:
                return x
        