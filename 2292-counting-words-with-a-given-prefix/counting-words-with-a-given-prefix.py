class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        for i in range(len(words)):
            word=words[i]
            if pref in word[0:len(pref)]:
                count +=1
        return (count)