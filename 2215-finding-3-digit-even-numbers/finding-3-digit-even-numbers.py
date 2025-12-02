class Solution(object):
    def findEvenNumbers(self, digits):
        result = set()
        
        n = len(digits)
        for i in range(n):             # hundreds place
            if digits[i] == 0:
                continue               # cannot start with 0
                
            for j in range(n):         # tens place
                if j == i:
                    continue

                for k in range(n):     # units place (must be even)
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i]*100 + digits[j]*10 + digits[k]
                    result.add(num)

        return sorted(result)
