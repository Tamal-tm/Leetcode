class Solution(object):
    def minimumLength(self, s):
        seen = {}
        count = 0

        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        for value in seen.values():
            if value % 2 == 0:
                count += 2
            else:
                count += 1

        return count
