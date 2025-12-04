
class Solution(object):
    def commonFactors(self, a, b):
        def gcd(a,b):
            count=0
            if a>b:
                return gcd(b,a)
            else:
                for i in range(1,a+1):
                    if b % i == 0 and a % i ==0:
                        count +=1
                return count
            
        res=gcd(a,b)
        return (res)