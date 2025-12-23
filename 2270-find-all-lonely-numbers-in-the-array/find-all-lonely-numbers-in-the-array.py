class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Frequency map
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        mylist = []
        for num in counts:
            # Appears only once and no adjacent numbers exist
            if counts[num] == 1 and (num + 1) not in counts and (num - 1) not in counts:
                mylist.append(num)
        
        return mylist
