class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)  # To reduce lookup time to O(1)
        dp = {n: 0}

        # Returns minimum number of extra characters in s starting from i
        def dfs(i):
            if i in dp:
                return dp[i]

            # skip
            res = 1 + dfs(i + 1)

            # take
            for j in range(i + 1, n + 1):
                if s[i: j] in words:
                    res = min(res, dfs(j))

            dp[i] = res
            return res

        return dfs(0)