class Solution(object):
    def minDeletion(self, s, k):
        if k >= len(set(s)):
            return 0

        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        # sort frequencies in ascending order
        freqs = sorted(seen.values())

        deletions = 0
        distinct = len(freqs)

        i = 0
        while distinct > k:
            deletions += freqs[i]
            distinct -= 1
            i += 1

        return deletions
