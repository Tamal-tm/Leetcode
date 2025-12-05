class Solution(object):
    def checkPrimeFrequency(self, nums):
        seen = {}
        
        # build frequency map
        for x in nums:
            if x in seen:
                seen[x] += 1
            else:
                seen[x] = 1

        # check if any frequency is prime
        for val in seen:
            freq = seen[val]

            if freq < 2:       # 0 or 1 → not prime
                continue

            # check primality of freq
            isPrime = True
            for d in range(2, int(freq**0.5) + 1):
                if freq % d == 0:
                    isPrime = False
                    break
            
            if isPrime:
                return True

        return False
