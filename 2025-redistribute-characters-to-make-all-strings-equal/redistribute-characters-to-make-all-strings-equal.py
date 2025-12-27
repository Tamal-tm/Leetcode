class Solution(object):
    def makeEqual(self, words):
        freq = {}
        n = len(words)

        for word in words:
            for ch in word:
                freq[ch] = freq.get(ch, 0) + 1

        for count in freq.values():
            if count % n != 0:
                return False

        return True
