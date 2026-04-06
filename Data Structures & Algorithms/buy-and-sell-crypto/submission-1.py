class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for price in prices:
            sell = price
            profit = sell - buy
            maxProfit = max(profit, maxProfit)
            buy = min(price, buy)

        return maxProfit
        