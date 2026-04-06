class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(i, runMax):
            if i >= n:
                return 0

            if (i, runMax) in cache:
                return cache[(i, runMax)]

            if nums[i] > runMax:
                l = max(
                        dfs(i + 1, nums[i]) + 1,   # take i
                        dfs(i + 1, runMax)    # skip i
                    )
            else:
                l = dfs(i + 1, runMax) # skip i

            cache[(i, runMax)] = l
            return l

        return dfs(0, float('-inf'))