class Solution(object):
    def totalNumbers(self, digits):
        num=set()

        for a,b,c in permutations(digits,3):
            if a!=0 and c%2==0:
                num.add((a,b,c))
        
        return len(num)
        