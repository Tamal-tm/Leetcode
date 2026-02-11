class Solution(object):
    def smallestNumber(self, n):
        store=bin(n)[2:]
        length=len(str(store))
        correct_val=0
        for i in range(0, length):
            correct_val = correct_val + (1*(2**i))

        return correct_val
        