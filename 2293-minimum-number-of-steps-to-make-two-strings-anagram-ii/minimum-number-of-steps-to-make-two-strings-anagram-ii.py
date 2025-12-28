class Solution(object):
    def minSteps(self, s, t):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            freq[ch] = freq.get(ch, 0) - 1

        steps = 0
        for v in freq.values():
            steps += abs(v)

        return steps
