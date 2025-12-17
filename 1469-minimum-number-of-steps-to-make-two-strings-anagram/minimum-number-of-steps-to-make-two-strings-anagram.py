class Solution(object):
    def minSteps(self, s, t):
        count = 0
        seen = {}

        # count characters of s
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1

        # try to match characters from t
        for ch in t:
            if ch in seen and seen[ch] > 0:
                seen[ch] -= 1
            else:
                count += 1

        return count
