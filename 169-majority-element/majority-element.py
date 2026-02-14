class Solution(object):
    def majorityElement(self, nums):
        freq = {}        # store frequencies
        n = 0            # highest count
        index = 0        # element with highest count

        for x in nums:
            # count efficiently instead of nums.count(x)
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

            # update max count and index
            if freq[x] > n:
                n = freq[x]
                index = x

        return index
