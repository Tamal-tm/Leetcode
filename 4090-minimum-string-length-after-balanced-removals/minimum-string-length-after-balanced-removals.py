class Solution(object):
    def minLengthAfterRemovals(self, s):
        seen={}
        check=set(s)
        if len(check) ==1:
            return len(s)
        
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] +=1
            else:
                seen[s[i]] =1
                
        value = list(seen.values())[0]
        value_2=list(seen.values())[1]
        
        if value == value_2:
            return 0
        else:
            return abs (value - value_2)