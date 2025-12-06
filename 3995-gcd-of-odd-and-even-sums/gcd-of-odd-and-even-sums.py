class Solution(object):
    def gcdOfOddEvenSums(self, n):
        res_sum =1
        value=0
        vales=0
        for i in range(1,n+1):
            value=i
            res_sum += value
        res_sum_2=res_sum+n
        for j in range(1,(res_sum+1)):
            if res_sum % j == 0 and res_sum_2 % j == 0:
                values=j
        return(value)
        