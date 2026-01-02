class Solution(object):
    def mostFrequentEven(self, nums):
        seen = {}
        
        for n in nums:
            if n % 2 == 0:
                if n in seen:
                    seen[n] += 1
                else:
                    seen[n] = 1
        
        if not seen:
            return -1
        
        max_freq = 0
        answer = float('inf')
        
        for key, value in seen.items():
            if value > max_freq or (value == max_freq and key < answer):
                max_freq = value
                answer = key
        
        return answer
