class Solution(object):
    def numTilePossibilities(self, tiles):
        from collections import Counter
        
        count = Counter(tiles)

        def dfs():
            total = 0
            for ch in count:
                if count[ch] > 0:
                    # choose this character
                    count[ch] -= 1
                    total += 1          # this forms one valid sequence
                    total += dfs()      # extend further
                    count[ch] += 1      # backtrack
            return total

        return dfs()
