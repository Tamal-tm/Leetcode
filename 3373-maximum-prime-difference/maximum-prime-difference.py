class Solution(object):
    def maximumPrimeDifference(self, nums):
        checkPrime = True
        mylist = []

        for i in range(len(nums)):
            val = nums[i]

            if val <= 1:
                checkPrime = False
            else:
                # optimised prime check (sqrt)
                for j in range(2, int(val**0.5) + 1):
                    if val % j == 0:
                        checkPrime = False
                        break

            if checkPrime == True:
                mylist.append(i)

            checkPrime = True   # reset

        if len(mylist) <= 1:
            return 0
        else:
            return mylist[-1] - mylist[0]
