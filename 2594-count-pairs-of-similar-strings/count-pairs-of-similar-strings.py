class Solution(object):
    def similarPairs(self, words):
        seen = {}
        count = 0

        for word in words:
            key = tuple(sorted(set(word)))

            if key in seen:
                count += seen[key]
                seen[key] += 1
            else:
                seen[key] = 1

        return count
