class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1 : 1}

        def dfs(num):
            if num in dp:
                return dp[num]

            res = 0 if num == n else num
            for i in range(1, num):
                res = max(res, dfs(i) * dfs(num - i))

            dp[num] = res
            return res

        return dfs(n)


        #                                                            12
        #          1, 11           2, 10           3, 9
        #    1, 10     2, 9
    

