class Solution(object):
    def digitCount(self, num):
        seen = {}

        # count digits
        for i in range(len(num)):
            if num[i] in seen:
                seen[num[i]] += 1
            else:
                seen[num[i]] = 1  

        # check digit count condition
        for i in range(len(num)):
            if seen.get(str(i), 0) != int(num[i]):
                return False
        
        return True
