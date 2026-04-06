class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        self.count = 0
        self.n_coins = float('inf')

        def dfs(i, curAmount, n_coins, count):
            if curAmount == amount:
                self.n_coins = min(self.n_coins, count)
            if curAmount > amount:
                return
            if i == len(coins):
                return

            # exclude
            dfs(i + 1, curAmount, n_coins, count)

            # include
            dfs(i, curAmount + coins[i], n_coins, count + 1)

        dfs(0, 0, self.n_coins, self.count)

        return -1 if self.n_coins == float('inf') else self.n_coins
