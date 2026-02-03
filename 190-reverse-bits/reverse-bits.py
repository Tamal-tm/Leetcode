class Solution(object):
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            # Extract the current last bit of n and place it in the reversed position
            ans |= (n & 1) << (31 - i)
            # Right shift n to process the next bit
            n >>= 1
        return ans

        