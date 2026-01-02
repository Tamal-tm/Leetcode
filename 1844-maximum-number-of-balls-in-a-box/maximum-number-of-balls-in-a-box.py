class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        seen = {}
        ans = 0

        for i in range(lowLimit, highLimit + 1):
            s = 0
            n = i
            while n > 0:
                s += n % 10
                n //= 10

            seen[s] = seen.get(s, 0) + 1
            ans = max(ans, seen[s])

        return ans
