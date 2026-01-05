class Solution(object):
    def maxFreqSum(self, s):
        vowels = {'a','e','i','o','u'}
        seen_v = {}
        seen_c = {}

        for ch in s:
            if ch in vowels:
                seen_v[ch] = seen_v.get(ch, 0) + 1
            else:
                seen_c[ch] = seen_c.get(ch, 0) + 1

        max_v = max(seen_v.values()) if seen_v else 0
        max_c = max(seen_c.values()) if seen_c else 0

        return max_v + max_c
