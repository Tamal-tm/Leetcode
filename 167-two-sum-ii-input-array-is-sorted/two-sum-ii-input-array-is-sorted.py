class Solution(object):
    def twoSum(self, numbers, target):
        seen={}        
        for i, num in enumerate(numbers):
            diff=target-num

            if diff in seen:
                return [seen[diff]+1,i+1]

            seen[num]=i
        
        