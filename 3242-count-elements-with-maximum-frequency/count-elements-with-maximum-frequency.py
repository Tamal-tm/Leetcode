class Solution(object):
    def maxFrequencyElements(self, nums):
        seen = {}
        
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        max_freq = max(seen.values())
        count = 0
        
        for v in seen.values():
            if v == max_freq:
                count += v
        
        return count
