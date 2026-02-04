class Solution(object):
    def hammingDistance(self, x, y):
        count = 0
        xor = x ^ y
        
        while xor:
            count += 1
            xor &= xor - 1   # removes lowest set bit
        
        return count
