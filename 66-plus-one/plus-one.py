class Solution(object):
    def plusOne(self, digits):
        mylist=[]
        result = int("".join(map(str,digits)))
        result +=1
        string=str(result)
        int_list = list(map(int, string))
        return int_list
        