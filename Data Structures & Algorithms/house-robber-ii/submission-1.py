class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(i, last):
            if i > last:
                return 0

            if (i, last) in cache:
                return cache[(i, last)]

            # skip i
            skip = dfs(i + 1, last)

            # include i 
            incl = dfs(i + 2, last) + nums[i]

            res = max(incl, skip)
            cache[(i, last)] = res
            return res

        return max(dfs(0, n - 2), dfs(1, n - 1))