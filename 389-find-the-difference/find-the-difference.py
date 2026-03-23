class Solution(object):
    def findTheDifference(self, s, t):
        seen1 = {}
        seen2 = {}

        # Count characters in s
        for ch in s:
            if ch in seen1:
                seen1[ch] += 1
            else:
                seen1[ch] = 1

        # Count characters in t
        for ch in t:
            if ch in seen2:
                seen2[ch] += 1
            else:
                seen2[ch] = 1

        # Find the character that has different count
        for ch in seen2:
            if ch not in seen1 or seen2[ch] != seen1.get(ch, 0):
                return ch