class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        seen = {}
        banned_words = set([w.lower() for w in banned])
        punct = "!?',;."

        # convert to lowercase
        paragraph = paragraph.lower()

        # replace punctuation with spaces
        for p in punct:
            paragraph = paragraph.replace(p, " ")

        # split on spaces
        words = paragraph.split()

        for word in words:
            if word == "" or word in banned_words:
                continue
            if word in seen:
                seen[word] += 1
            else:
                seen[word] = 1

        max_key = max(seen, key=seen.get)
        print(seen)
        return max_key
