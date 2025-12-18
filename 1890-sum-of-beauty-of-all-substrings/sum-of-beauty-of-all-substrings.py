class Solution(object):
    def beautySum(self, s):
        n = len(s)
        res = 0

        for i in range(n):
            freq = {}
            for j in range(i, n):
                ch = s[j]
                freq[ch] = freq.get(ch, 0) + 1

                max_val = max(freq.values())
                min_val = min(freq.values())
                res += max_val - min_val

        return res
