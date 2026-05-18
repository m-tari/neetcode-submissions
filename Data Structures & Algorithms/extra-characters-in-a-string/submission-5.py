class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = {}

        def dfs(i):
            if i == n:
                return 0

            if i in dp:
                return dp[i]

            # skip
            res = 1 + dfs(i + 1)

            for w in dictionary:
                if w == s[i: i + len(w)]:
                    res = min(res, dfs(i + len(w)))

            dp[i] = res
            return res

        return dfs(0)