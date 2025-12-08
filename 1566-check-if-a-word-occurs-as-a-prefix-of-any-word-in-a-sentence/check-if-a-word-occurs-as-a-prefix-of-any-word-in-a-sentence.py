class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        sentence = sentence.split()
        for i in range(len(sentence)):
            # FIX: check prefix, not substring
            if sentence[i].startswith(searchWord):
                return i + 1
        return -1
