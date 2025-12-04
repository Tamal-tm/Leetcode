class Solution(object):
    def countBeautifulPairs(self, nums):

        # helper to get gcd 
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        res = 0
        n = len(nums)

        for i in range(n):
            # first digit of nums[i]
            first = int(str(nums[i])[0])
            
            for j in range(i+1, n):
                # last digit of nums[j]
                last = nums[j] % 10
                
                if gcd(first, last) == 1:
                    res += 1
                    
        return res


# test