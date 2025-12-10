class Solution(object):
    def repeatedStringMatch(self, a, b):
        value_1 = len(b)
        value_2 = len(a)

        short = value_1 // value_2

        
        if b in (a * short):
            return short
        if b in (a * (short + 1)):
            return short + 1
        if b in (a * (short + 2)):
            return short + 2

        return -1
