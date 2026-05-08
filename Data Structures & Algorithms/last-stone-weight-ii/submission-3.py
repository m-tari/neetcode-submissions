class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = {}

        # We separate the stones in two groups, positives and negatives.
        # Then we find the minimum w for the combination of items belonging to positive or negative groups.

        def dfs(i, cur_w):
            if i == n:
                return abs(cur_w)  # Only the abs matters. If it's negative, it means we should switch the groups

            if (i, cur_w) in dp:
                return dp[(i, cur_w)]

            # Assign i to the positive group
            pos = dfs(i + 1, cur_w + stones[i])
            # Assign i to the negative group
            neg = dfs(i + 1, cur_w - stones[i])

            dp[(i, cur_w)] = min(pos, neg)
            return dp[(i, cur_w)]

        return dfs(0, 0)