class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        # clean and split both sentences
        word1 = s1.strip().lower().split()
        word2 = s2.strip().lower().split()

        # combine both word lists
        all_words = word1 + word2

        # count occurrences manually
        seen = {}
        for w in all_words:
            if w in seen:
                seen[w] += 1
            else:
                seen[w] = 1

        # collect words that appear only once
        result = []
        for w in seen:
            if seen[w] == 1:
                result.append(w)

        return result