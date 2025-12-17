class Solution(object):
    def minSteps(self, s, t):
        count = 0
        seen = {}

        # build frequency map for s
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1

        # process t
        for i in range(len(t)):
            if t[i] in seen and seen[t[i]] > 0:
                seen[t[i]] -= 1
            else:
                count += 1

        return count
