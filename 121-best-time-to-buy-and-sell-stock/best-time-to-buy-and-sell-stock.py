class Solution(object):
    def maxProfit(self, prices):
        min_price=float("inf")
        max_profit=0
        n=len(prices)
        for i in range(n):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit