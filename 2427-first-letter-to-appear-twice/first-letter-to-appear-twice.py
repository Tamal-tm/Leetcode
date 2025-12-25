class Solution(object):
    def repeatedCharacter(self, s):
        seen={}
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] +=1
                return s[i]
            else:
                seen[s[i]]=1