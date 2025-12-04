class Solution(object):
    def kthFactor(self, n, k):
        mid= n//2 + 1
        mylist=[]
        for i in range(1, mid):
            if n % i == 0:
                mylist.append(i)
        mylist.append(n)
        if k > len(mylist):
            return -1 
        else:
            return mylist[k-1]