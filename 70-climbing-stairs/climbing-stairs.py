class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        a, b = 1, 2   # ways(1)=1, ways(2)=2
        for i in range(3, n + 1):
            a, b = b, a + b   # ways(n)=ways(n-1)+ways(n-2)
        return b
