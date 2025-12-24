class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        freq = [0] * 26

        for c in word1:
            freq[ord(c) - 97] += 1

        for c in word2:
            freq[ord(c) - 97] -= 1

        for v in freq:
            if v > 3 or v < -3:
                return False

        return True
