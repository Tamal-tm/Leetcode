class Solution(object):
    def findLucky(self, arr):
        seen={}
        mylist=[]
        for i in range(len(arr)):
            if arr[i] in seen:
                seen[arr[i]] +=1
            else:
                seen[arr[i]] =1
        
        for key, value in seen.items():
            if key == value:
                mylist.append(key)
        
        if len(mylist) !=0:
            return max(mylist)
        else:
            return -1