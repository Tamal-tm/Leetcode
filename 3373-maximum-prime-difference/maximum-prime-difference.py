class Solution(object):
    def maximumPrimeDifference(self, nums):
        mylist = []

        for i in range(len(nums)):
            val = nums[i]

            # Skip 1 immediately
            if val <= 1:
                continue

            # Prime check (optimized)
            isPrime = True
            for j in range(2, int(val**0.5) + 1):   # check only till sqrt(val)
                if val % j == 0:
                    isPrime = False
                    break

            # If prime → record index
            if isPrime:
                mylist.append(i)

        # Return difference
        if len(mylist) <= 1:
            return 0
        return mylist[-1] - mylist[0]
