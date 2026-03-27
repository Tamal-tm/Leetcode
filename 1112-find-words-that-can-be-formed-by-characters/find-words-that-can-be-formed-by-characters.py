class Solution(object):
    def countCharacters(self, words, chars):
        total = 0

        for word in words:
            good = True
            temp_chars = list(chars)  # make a copy of chars to use each letter once
            for ch in word:
                if ch in temp_chars:
                    temp_chars.remove(ch)
                else:
                    good = False
                    break
            if good:
                total += len(word)

        return total