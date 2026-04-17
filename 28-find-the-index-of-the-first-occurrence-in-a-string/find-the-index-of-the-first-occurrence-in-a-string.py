class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        n = len(needle)
        h = len(haystack)

        # loop through possible starting positions
        for i in range(h - n + 1):
            # check substring match
            if haystack[i:i+n] == needle:
                return i
        return -1


            