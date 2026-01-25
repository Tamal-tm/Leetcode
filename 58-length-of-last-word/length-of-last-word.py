class Solution(object):
    def lengthOfLastWord(self, s):
        trimmed=s.strip()
        a=trimmed.split(" ")
        size=len(a)
        last_word=a[size-1]
        c=0
        for i in range(len(last_word)):
            c += 1
        return c            
        