class Solution(object):
    def rearrangeArray(self, nums):
        mylist = []
        left_plus = []
        right_minus = []

        # separate positives and negatives
        for num in nums:
            if num > 0:
                left_plus.append(num)
            else:
                right_minus.append(num)

        # merge alternately (problem guarantees equal count)
        i = 0
        while i < len(left_plus):
            mylist.append(left_plus[i])
            mylist.append(right_minus[i])
            i += 1

        return mylist
