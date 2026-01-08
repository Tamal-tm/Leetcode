class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        new_str = ""
        seen = {}

        # sort string in descending order
        sorted_s = "".join(sorted(s, reverse=True))

        # count frequency
        for i in range(len(sorted_s)):
            if sorted_s[i] in seen:
                seen[sorted_s[i]] += 1
            else:
                seen[sorted_s[i]] = 1

        keys = sorted(seen.keys(), reverse=True)

        i = 0
        while i < len(keys):
            ch = keys[i]

            use = min(seen[ch], repeatLimit)
            new_str += ch * use
            seen[ch] -= use

            if seen[ch] > 0:
                # need a smaller character to break repetition
                if i + 1 >= len(keys):
                    break
                next_ch = keys[i + 1]
                new_str += next_ch
                seen[next_ch] -= 1

                if seen[next_ch] == 0:
                    keys.pop(i + 1)
            else:
                i += 1

        return new_str
