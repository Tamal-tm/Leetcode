class Solution(object):
    def doesAliceWin(self, s):
        count=0
        vowels={'a','e','i','o','u'}
        for i in range(len(s)):
            if s[i] in vowels:
                count +=1
        
        
        if count >= 1:
            return True
        else:
            return False