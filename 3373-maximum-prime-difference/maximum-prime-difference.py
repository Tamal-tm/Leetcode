class Solution(object):
    def maximumPrimeDifference(self, nums):
        checkPrime = True
        mylist = []

        for i in range(len(nums)):
            val = nums[i]

            # Skip small non-primes
            if val < 2:
                checkPrime = False
            else:
                # Check divisors only up to sqrt(val)
                for j in range(2, int(val**0.5) + 1):
                    if val % j == 0:
                        checkPrime = False
                        break

            # If prime, store index
            if checkPrime:
                mylist.append(i)

            checkPrime = True  # reset

        # If we have less than 2 primes
        if len(mylist) <= 1:
            return 0
        
        return mylist[-1] - mylist[0]
