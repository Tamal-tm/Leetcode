class Solution(object):
    def combinationSum2(self, candidates, target):
        
        nums = sorted(candidates)
        n = len(nums)
        result = []
        
        def backtrack(index, total, subset):
            
            if total == 0:
                result.append(subset[:])
                return
            
            if total < 0:
                return
            
            if index >= n:
                return
            
            for i in range(index, n):
                
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                subset.append(nums[i])
                Sum = total - nums[i]
                
                backtrack(i+1, Sum, subset)
                
                subset.pop()
        
        backtrack(0, target, [])
        
        return result