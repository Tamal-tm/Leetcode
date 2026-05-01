class Solution(object):
    def fib(self, n):
        a=0
        b=1
        f_sum=0
        if n == 0 or n == 1:
            return n    
        for i in range(n-1):
            c=a+b
            a=b 
            b=c 
            if i == n-1 or i == n-2:
                f_sum +=c
        return (f_sum)