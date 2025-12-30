class Solution(object):
    def countDistinctIntegers(self, nums):
        mylist=nums
        for i in range(len(nums)):
            str_num=str(nums[i])
            rev=str_num[::-1]
            str_int=int(rev)
            mylist.append(str_int)
        count=len(set(mylist))
        return (count)