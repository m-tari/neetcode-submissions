class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        
        for price in prices:
            sell = price
            profit = sell - buy
            if profit > maxProfit:
                maxProfit = profit
            if price < buy:
                buy = price


        return maxProfit
        