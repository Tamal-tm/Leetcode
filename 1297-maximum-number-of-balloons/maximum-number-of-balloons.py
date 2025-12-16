from collections import defaultdict
class Solution(object):
    def maxNumberOfBalloons(self, text):
        count = defaultdict(int)
        ans = 0
        for i in text:
            count[i] += 1

        a = count["a"] // 1 
        b = count["b"] // 1  
        l = count["l"] // 2  
        o = count["o"] // 2  
        n = count["n"] // 1
        
        return min(b, a, l, o, n) 