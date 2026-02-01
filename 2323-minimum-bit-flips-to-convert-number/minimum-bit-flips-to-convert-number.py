class Solution(object):
    def minBitFlips(self, start, goal):
        count=0
        ans=start^goal
        for i in range(0,32):
            if ((ans>>i)&1) == 1:
                count+=1
        return count        