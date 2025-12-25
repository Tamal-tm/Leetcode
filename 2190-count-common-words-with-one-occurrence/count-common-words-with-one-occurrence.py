class Solution(object):
    def countWords(self, words1, words2):
        seen1 = {}
        seen2 = {}
        count = 0

        for w in words1:
            seen1[w] = seen1.get(w, 0) + 1

        for w in words2:
            seen2[w] = seen2.get(w, 0) + 1

        for w in seen1:
            if seen1[w] == 1 and seen2.get(w, 0) == 1:
                count += 1

        return count
