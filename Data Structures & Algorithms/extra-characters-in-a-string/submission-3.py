class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)  # i
        d = len(dictionary)  # j
        dp = {}

        def dfs(i, coverage):
            if i == n:
                return coverage

            if (i, coverage) in dp:
                return dp[(i, coverage)]

            # take the character
            take = 0
            for w in dictionary:
                if w == s[i: i + len(w)]:
                    take = max(take, dfs(i + len(w), coverage + len(w)))

            res = max(take, dfs(i + 1, coverage))
            dp[(i, coverage)] = res
            return res

        return n - dfs(0, 0)