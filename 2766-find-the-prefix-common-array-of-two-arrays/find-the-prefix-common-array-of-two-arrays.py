class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        new_list=[]
        mylist=[]
        count=0
        for i in range(len(A)):
            if A[i] == B[i]:
                count +=1
            else:
                if A[i] in mylist:
                    count +=1
                if B[i] in mylist:
                    count +=1
            new_list.append(count)
            mylist.append(A[i])
            mylist.append(B[i])
        
        return new_list