class Solution(object):
    def countTriplets(self, arr):
        prefix = 0
        ans = 0
        
        count = {0: 1}
        total_index = {0: 0}
        
        for i in range(len(arr)):
            prefix ^= arr[i]
            
            if prefix in count:
                ans += count[prefix] * i - total_index[prefix]
            
            count[prefix] = count.get(prefix, 0) + 1
            total_index[prefix] = total_index.get(prefix, 0) + (i + 1)
        
        return ans
