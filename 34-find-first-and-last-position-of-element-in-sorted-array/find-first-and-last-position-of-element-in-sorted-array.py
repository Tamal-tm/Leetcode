class Solution(object):
    def searchRange(self, nums, target):
        mylist = []
        c = 0
        
        # Edge case: empty nums list
        if not nums:
            return [-1, -1]
        
        # Collect all indices where target occurs
        for i in range(len(nums)):
            if target == nums[i]:
                mylist.append(i)
                c += 1
                a = i  # store last index of target
        
        # If target not found at all
        if not mylist:
            return [-1, -1]
        
        # If only one occurrence
        elif c == 1:
            mylist.append(a)
            return mylist
        
        # If multiple occurrences
        else:
            first = mylist[0]
            last = mylist[-1]
            return [first, last]
