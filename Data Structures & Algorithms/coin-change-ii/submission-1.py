class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}

        def dfs(curAmount, i):
            if curAmount == 0:
                return 1

            if (curAmount, i) in cache:
                return cache[(curAmount, i)]

            if curAmount < 0 or i == len(coins):
                return 0

            incl = dfs(curAmount -  coins[i], i)
            excl = dfs(curAmount, i + 1)
            res = incl + excl

            cache[(curAmount, i)] = res
            return cache[(curAmount, i)]

        res = dfs(amount, 0)

        return res
