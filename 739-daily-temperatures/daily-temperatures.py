class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = []   # will store indices
        ans = [0] * n
        
        for i in range(n - 1, -1, -1):
            
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1] - i
            
            stack.append(i)
        return ans