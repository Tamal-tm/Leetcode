class Solution(object):
    def countConsistentStrings(self, allowed, words):
        
        ans = 0

        for i in words:
            able = True
            for j in i:
                if j not in allowed:
                    able = False
                    break
            if able:
                ans += 1
        
        return ans
