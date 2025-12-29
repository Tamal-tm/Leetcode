class Solution(object):
    def longestPalindrome(self, words):
        freq = {}
        length = 0
        center = False

        # Count frequencies
        for w in words:
            freq[w] = freq.get(w, 0) + 1

        for w in freq:
            rev = w[::-1]

            if w == rev:
                # Pair same-letter words
                pairs = freq[w] // 2
                length += pairs * 4
                if freq[w] % 2 == 1:
                    center = True
            elif w < rev and rev in freq:
                # Pair reversible words only once
                pairs = min(freq[w], freq[rev])
                length += pairs * 4

        if center:
            length += 2

        return length
