class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        for word in words:
            if pref in word[0:len(pref)]:
                count +=1
        return (count)

        c = 0
        n = len(pref)
        for word in words:
            if pref in word[0:n]:
               c+=1
        return c