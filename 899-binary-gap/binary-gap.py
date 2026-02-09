class Solution(object):
    def binaryGap(self, n):
        val=str(bin(n)[2:])
        count=0
        max_count=0
        flag=0
        for i in range(0, len(val)):
            
            if val[i] == '1':
                flag +=1
                if flag ==2:
                    max_count=max(max_count,count)
                    count=1
                    flag=1
                else:
                    count =1
            else:
                count +=1
            

        return max_count