class Solution(object):
    def findGCD(self, nums):
        min_num=min(nums)
        max_num=max(nums)
        def gcd(min_num,max_num):
            if min_num > max_num:
                return gcd(min_num, max_num)
            else:
                for i in range(1,min_num+1):
                    if min_num % i == 0 and max_num % i == 0:
                        store = i 
                return store
        res=gcd(min_num,max_num)
        return res