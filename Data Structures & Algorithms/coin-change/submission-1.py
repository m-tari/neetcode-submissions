class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)
        cache = [[float('inf')] * (amount + 1) for _ in range(N)]

        def dfs(i, curAmount):

            if curAmount == amount:
                return 0
            if i == N:
                return float('inf')
            if cache[i][curAmount] != float('inf'):
                return cache[i][curAmount]
            
            # exclude
            exclude = dfs(i + 1, curAmount)

            # include
            include = float('inf')
            if curAmount + coins[i] <= amount: 
                include = dfs(i, curAmount + coins[i]) + 1

            cache[i][curAmount] = min(include, exclude)

            return cache[i][curAmount]

        res = dfs(0, 0)

        return -1 if res == float('inf') else res
