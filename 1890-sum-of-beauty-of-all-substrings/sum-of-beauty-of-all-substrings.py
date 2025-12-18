class Solution(object):
    def beautySum(self, s):
        n = len(s)
        res = 0

        for i in range(n):
            seen = {}

            for j in range(i, n):
                ch = s[j]
                if ch in seen:
                    seen[ch] += 1
                else:
                    seen[ch] = 1

                max_freq = max(seen.values())
                min_freq = min(seen.values())

                res += (max_freq - min_freq)

        return res
