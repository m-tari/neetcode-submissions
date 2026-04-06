class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        # state: i: current index, j: the index of last included element in the subsequence

        def dfs(i, j):
            if i == n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if j == -1 or nums[i] > nums[j]:
                l = max(
                        dfs(i + 1, i) + 1,   # take i
                        dfs(i + 1, j)    # skip i
                    )
            else:
                l = dfs(i + 1, j) # skip i

            cache[(i, j)] = l
            return l

        return dfs(0, -1)