class Solution(object):
    def minNumberOperations(self, target):
        prev = 0
        res = 0
        for num in target:
            if num > prev:
                res += num-prev
            prev = num
        return res

            
