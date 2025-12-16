class Solution(object):
    def maxNumberOfBalloons(self, text):
        letters = "balloon"
        seen = {}
        count = 0
        real_count = 0

        # count letters
        for i in range(len(text)):
            if text[i] in letters:
                if text[i] in seen:
                    seen[text[i]] += 1
                else:
                    seen[text[i]] = 1

        # keep forming "balloon"
        while True:
            for ch in letters:
                if ch not in seen or seen[ch] == 0:
                    return real_count
                seen[ch] -= 1

            real_count += 1
