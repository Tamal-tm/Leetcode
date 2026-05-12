class Solution(object):
    def reorganizeString(self, s):
        # count frequency
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        # check if possible
        if max(seen.values()) > (len(s) + 1) // 2:
            return ""

        # make a list of characters repeated by their frequency
        chars = sorted(seen.keys(), key=lambda x: -seen[x])
        res = [""] * len(s)

        i = 0
        for ch in chars:
            for _ in range(seen[ch]):
                res[i] = ch
                i += 2
                if i >= len(s):  # once even places are filled, move to odd
                    i = 1

        return "".join(res)