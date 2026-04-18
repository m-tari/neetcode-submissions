class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def dfs(i, canSell):
            if i == n:
                return 0

            if (i, canSell) in dp:
                return dp[(i, canSell)]

           # sell
            if canSell:
                sell = dfs(i + 1, False) + prices[i]

            # buy (We can only buy if we are not already holding a stock)
            if not canSell:
                buy = dfs(i + 1,  True) - prices[i]

            # skip
            skip = dfs(i + 1, canSell)

            res = max(sell, skip) if canSell else max(buy, skip)
            dp[(i, canSell)] = res
            return res
        
        return dfs(0, False)





#                                        buy/sell/skip   
#   i = 0                    -7                   0                   0
#   i = 1             -8   -6  -7       -1   0    0          -1 0  0
#   i = 2                                -6 4 -1

                        