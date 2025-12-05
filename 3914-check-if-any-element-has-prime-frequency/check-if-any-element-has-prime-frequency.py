class Solution(object):
    def checkPrimeFrequency(self, nums):
        # build frequency map
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        # check if ANY frequency is prime
        for j in seen:                     # j = number
            freq = seen[j]                # frequency of that number

            if freq < 2:                  # 0 or 1 are NOT prime
                continue

            # check prime
            is_prime = True
            for k in range(2, int(freq**0.5) + 1):
                if freq % k == 0:
                    is_prime = False
                    break

            if is_prime:
                return True

        return False
