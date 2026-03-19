class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        res = [0] * n
        positions = []

        # Step 1: Store all indices of character c
        for i in range(n):
            if s[i] == c:
                positions.append(i)

        # Step 2: Compute distance for each index
        for i in range(n):
            # Distance to nearest c
            min_dist = n  # initialize with max possible
            for pos in positions:
                min_dist = min(min_dist, abs(i - pos))
            res[i] = min_dist

        return res