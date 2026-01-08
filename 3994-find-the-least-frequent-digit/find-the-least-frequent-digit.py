class Solution(object):
    def getLeastFrequentDigit(self, n):
        freq = {}

        for ch in str(n):
            freq[ch] = freq.get(ch, 0) + 1

        min_freq = min(freq.values())
        ans = '9'

        for d in freq:
            if freq[d] == min_freq:
                ans = min(ans, d)

        return int(ans)
