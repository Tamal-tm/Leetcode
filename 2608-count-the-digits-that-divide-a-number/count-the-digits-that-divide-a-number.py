class Solution(object):
    def countDigits(self, num):
        str_num=str(num)
        count=0
        res=""
        for i in range(len(str_num)):
            get_num=int(str_num[i])
            
            if num % get_num == 0:
                count +=1
                res += str(get_num)
        return count