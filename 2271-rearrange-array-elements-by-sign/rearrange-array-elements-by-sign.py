class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        res = [0] * n
        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                res[pos] = num
                pos += 2
            else:
                res[neg] = num
                neg += 2

        return res
