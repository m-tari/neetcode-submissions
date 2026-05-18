class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = {}

        def dfs(i):
            if i == n:
                return 0

            if i in dp:
                return dp[i]

            take = 0
            for w in dictionary:
                if w == s[i: i + len(w)]:
                    take = max(take, len(w) + dfs(i + len(w)))

            res = max(take, dfs(i + 1))
            dp[i] = res
            return res

        return n - dfs(0)