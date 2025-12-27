class Solution(object):
    def makeEqual(self, words):
        freq = {}
        n = len(words)

        for w in words:
            for c in w:
                freq[c] = freq.get(c, 0) + 1

        for v in freq.values():
            if v % n != 0:
                return False

        return True
