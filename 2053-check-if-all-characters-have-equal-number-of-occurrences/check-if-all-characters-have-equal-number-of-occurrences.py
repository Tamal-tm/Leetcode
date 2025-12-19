class Solution(object):
    def areOccurrencesEqual(self, s):
        seen = {}

        # Count frequency
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1

        # Get all counts
        values = list(seen.values())

        # Check if all counts are same
        return len(set(values)) == 1
