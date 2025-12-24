class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1

        for i in range(26):
            c = chr(ord('a') + i)
            if abs(freq1.get(c, 0) - freq2.get(c, 0)) > 3:
                return False

        return True
