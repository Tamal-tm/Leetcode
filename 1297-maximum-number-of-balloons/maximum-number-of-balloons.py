class Solution(object):
    def maxNumberOfBalloons(self, text):
        seen = {}

        # Count characters
        for ch in text:
            seen[ch] = seen.get(ch, 0) + 1

        # Calculate how many "balloon"s we can form
        return min(
            seen.get('b', 0),
            seen.get('a', 0),
            seen.get('l', 0) // 2,
            seen.get('o', 0) // 2,
            seen.get('n', 0)
        )
