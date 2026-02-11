class Solution(object):
    def findArray(self, pref):
        n = len(pref)
        ans = [pref[0]]
        
        for i in range(1, n):
            ans.append(pref[i] ^ pref[i - 1])
        
        return ans
