class Solution(object):
    def duplicateNumbersXOR(self, nums):
        freq={}
        mylist=[]
        xor_val = 0
        for x in nums:
            if x in freq:
                freq[x] +=1
            else:
                freq[x] =1
                m=freq[x]
        
        for x in freq:
            if freq[x]==2:
                mylist.append(x)
            
        for num in mylist:
            xor_val ^= num

        return xor_val
        