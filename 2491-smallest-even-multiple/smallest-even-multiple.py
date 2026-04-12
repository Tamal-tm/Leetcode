class Solution(object):
    def smallestEvenMultiple(self, n):
        for i in range(1,9):
            a=n*i
            if a % 2 ==0:
                return a

        