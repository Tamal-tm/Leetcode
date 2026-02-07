class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}  # store last index of each number
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num in index_map:
                # if the distance between current and last index <= k
                if i - index_map[num] <= k:
                    return True
            
            # update last index of num
            index_map[num] = i
        
        return False
