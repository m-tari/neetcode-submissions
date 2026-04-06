class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i, canBuy):
            if i > n - 1:
                return 0

            sell = 0
            # sell
            if not canBuy:
                sell = dfs(i + 2, True) + prices[i]
        
            buy = 0
            # buy
            if canBuy:
                buy = dfs(i + 1, False) - prices[i]

            # skip
            skip = dfs(i + 1, canBuy)

            return max(buy, skip, sell)


        return dfs(0, True)