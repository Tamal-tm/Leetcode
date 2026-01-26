class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        s=s.strip()
        words.reverse()
        word=" ".join(words)
        return(word)