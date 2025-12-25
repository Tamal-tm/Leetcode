class Solution(object):
    def digitCount(self, num):
        seen = {}

        for ch in num:
            seen[ch] = seen.get(ch, 0) + 1

        for i in range(len(num)):
            if seen.get(str(i), 0) != int(num[i]):
                return False

        return True
