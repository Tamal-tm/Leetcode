class Solution(object):
    def areOccurrencesEqual(self, s):
        seen = {}

        # count frequency
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1

        # get first frequency as reference
        first_value = list(seen.values())[0]

        # compare all frequencies
        for ch in seen:
            if seen[ch] != first_value:
                return False

        return True
