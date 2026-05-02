class Solution(object):
    def countSegments(self, s):
        count = 0
        in_word = False

        for ch in s:
            if ch != ' ':
                if not in_word:      # we just entered a word
                    count += 1
                    in_word = True
            else:
                in_word = False      # we left a word

        return count