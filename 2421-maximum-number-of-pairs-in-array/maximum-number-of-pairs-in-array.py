from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = Counter(nums)
        pairs_count = 0
        leftovers_count = 0
        
        for count in counts.values():
            # For each number's frequency, the number of pairs is integer division by 2
            pairs_count += count // 2
            # The number of leftovers is the remainder after division by 2 (0 or 1)
            leftovers_count += count % 2
            
        # Return the result as a list [number of pairs, number of leftover elements]
        return [pairs_count, leftovers_count]
