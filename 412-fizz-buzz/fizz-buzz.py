class Solution(object):
    def fizzBuzz(self, n):
        list1=[]
        i=1
        while i<=n:
            if i % 3 == 0 and i % 5 == 0:
                list1.append("FizzBuzz")

            elif i % 3 == 0:
                list1.append("Fizz")

            elif i % 5 == 0:
                list1.append("Buzz")

            else:
                list1.append(str(i))
            i+= 1
        return list1

n=5
s=Solution()
result=s.fizzBuzz(n)

        
        
        
        
        
        