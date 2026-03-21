def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n
        
        while left <= right:
            num = (left + right) // 2   # middle number
            p = guess(num)
            
            if p == 0:
                return num        # correct guess
            elif p == -1:
                right = num - 1   # too high
            else:
                left = num + 1    # too low