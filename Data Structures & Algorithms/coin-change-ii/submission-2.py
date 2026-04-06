class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}

        def dfs(remaining, i):
            if remaining == 0:
                return 1

            if (remaining, i) in cache:
                return cache[(remaining, i)]

            if remaining < 0 or i == len(coins):
                return 0

            # incl = dfs(remaining -  coins[i], i)
            # excl = dfs(remaining, i + 1)
            # ways = incl + excl
            # Instead of incl, excl appoach, you can iterate on coins too
            # But you should start from i in order to have distinct combinations
            ways = 0
            for j in range(i, len(coins)):
                ways += dfs(remaining -  coins[j], j)

            cache[(remaining, i)] = ways
            return ways

        return dfs(amount, 0)
