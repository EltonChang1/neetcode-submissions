class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        cheapest = prices[0]

        for i in prices:
            if i < cheapest:
                cheapest = i
            profit = i - cheapest
            if profit > maxprofit:
                maxprofit = profit
        
        return maxprofit