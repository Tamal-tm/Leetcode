class Solution(object):
    def selfDividingNumbers(self, left, right):
        mylist=[]
        for i in range(left, right+1):
            c=0
            real_num=i
            while i!=0:
                num=i%10
                if num == 0:
                    c=1
                    break
                elif real_num % num ==0:
                    i =i//10
                else:
                    c=1
                    break
            if c==0:
                mylist.append(real_num)
        return mylist