class Solution(object):
    def findLucky(self, arr):
        seen = {}
        mylist = []

        for i in range(len(arr)):
            if arr[i] in seen:
                seen[arr[i]] += 1
            else:
                seen[arr[i]] = 1

        for key in seen:
            if key == seen[key]:
                mylist.append(key)

        if mylist:
            return max(mylist)
        return -1
