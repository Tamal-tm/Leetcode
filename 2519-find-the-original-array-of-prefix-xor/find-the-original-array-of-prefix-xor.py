class Solution(object):
    def findArray(self, pref):
        mylist = []
        
        for i in range(len(pref)):
            if i == 0:
                mylist.append(pref[i])
            else:
                mylist.append(pref[i] ^ pref[i - 1])
        
        return mylist
