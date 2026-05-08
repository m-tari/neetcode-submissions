class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = {}

        def dfs(i, cur_w):
            if i == n:
                return cur_w

            if (i, cur_w) in dp:
                return dp[(i, cur_w)]

            # Assign i to positive group
            pos = dfs(i + 1, cur_w + stones[i])

            # Assign i to negative group
            neg = dfs(i + 1, cur_w - stones[i])

            if pos >= 0 and neg >= 0:
                res = min(pos, neg)
            elif pos >= 0 and neg < 0:
                res = pos
            elif pos < 0 and neg >= 0:
                res = neg
            else:
                res = float('inf')

            dp[(i, cur_w)] = res
            return res
        
        
        return dfs(0, 0)