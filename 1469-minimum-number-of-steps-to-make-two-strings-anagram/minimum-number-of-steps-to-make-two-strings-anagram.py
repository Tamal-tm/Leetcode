class Solution(object):
    def minSteps(self, s, t):
        count=0
        for i in range(len(t)):
            if t[i] in s:
                index_pos=s.index(t[i])
                s = s[:index_pos] + s[index_pos+1:]
            else:
                count +=1
        return (count)
        