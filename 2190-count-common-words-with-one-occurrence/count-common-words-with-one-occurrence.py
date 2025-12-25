class Solution(object):
    def countWords(self, words1, words2):
        count = 0
        seen1 = {}
        seen2 = {}

        for word in words1:
            if word in seen1:
                seen1[word] += 1
            else:
                seen1[word] = 1

        for word in words2:
            if word in seen2:
                seen2[word] += 1
            else:
                seen2[word] = 1

        for word in seen1:
            if seen1[word] == 1 and seen2.get(word, 0) == 1:
                count += 1

        return count
