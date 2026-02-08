class Solution(object):
    def isIsomorphic(self, s, t):
        seen = {}
        seen2 = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            # check existing mappings
            if ch1 in seen:
                if seen[ch1] != ch2:
                    return False
            else:
                seen[ch1] = ch2

            if ch2 in seen2:
                if seen2[ch2] != ch1:
                    return False
            else:
                seen2[ch2] = ch1

        return True
