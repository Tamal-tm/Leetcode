class Solution(object):
    def divisorGame(self, n):
        count = 0
        
        while n > 1:
            # find the first valid divisor x < n
            for i in range(1, n):
                if n % i == 0:
                    n -= i     # Alice or Bob makes one move
                    count += 1
                    break      # IMPORTANT: break after ONE move
        
        # if count is odd → Alice made last move → Alice wins
        return count % 2 == 1