class Solution(object):
    def evenOddBit(self, n):
        even_count=0
        odd_count=0
        for i in range(0,16):
            if i % 2 == 0:
                if n & (1<<i):
                    even_count +=1
            else:
                if n & (1<<i):
                    odd_count +=1
        
        return [even_count, odd_count]

        