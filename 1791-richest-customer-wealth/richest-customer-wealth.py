class Solution(object):
    def maximumWealth(self, accounts):
        s = 0
        m = 0
        for banks in accounts:
            s = 0
            for amount in banks:
                s += amount
            if s > m:
                m = s
        return m


        