class Solution(object):
    def mostFrequentEven(self, nums):
        seen = {}
        max_freq = 0
        result = -1

        for n in nums:
            if n % 2 == 0:
                seen[n] = seen.get(n, 0) + 1

                if seen[n] > max_freq or (seen[n] == max_freq and n < result):
                    max_freq = seen[n]
                    result = n

        return result
