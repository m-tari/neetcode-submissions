class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        new_nums = [1] + nums + [1]
        cache = {}  # (l, r) -> maxCoins

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            res = 0
            for i in range(l, r + 1):
                coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                coins += dfs(l, i - 1)
                coins += dfs(i + 1, r)
                res = max(res, coins)

            cache[(l, r)] = res
            return res
        
        return dfs(1, len(new_nums) - 2)
            

#       l           r    
# [1, 4, 2, 3, 7, 1]