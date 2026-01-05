class Solution(object):
    def maxFreqSum(self, s):
        vowels=('a','e','i','o','u')
        seen={}
        max_val=max_val2=0
        seen2={}
        for i in range(len(s)):
            if s[i] in vowels:
                if s[i] in seen:
                    seen[s[i]] +=1
                else:
                    seen[s[i]] =1
            else:
                if s[i] in seen2:
                    seen2[s[i]] +=1
                else:
                    seen2[s[i]] =1
        if seen2.values():
            max_val2 = max(seen2.values())
        else:
            max_val2 = 0
        if seen.values():
            max_val = max(seen.values())
        else:
            max_val = 0
        
        return max_val+max_val2