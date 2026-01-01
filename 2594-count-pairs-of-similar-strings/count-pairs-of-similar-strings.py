class Solution(object):
    def similarPairs(self, words):
        seen = {}
        count = 0

        for w in words:
            key = frozenset(w)

            if key in seen:
                count += seen[key]
                seen[key] += 1
            else:
                seen[key] = 1

        return count
