class Solution(object):
    def largestCombination(self, candidates):
        max_count = 0
        for bit in range(32):
            count = 0
            for num in candidates:
                if num & (1 << bit):
                    count += 1
            max_count = max(max_count, count)
        return max_count
