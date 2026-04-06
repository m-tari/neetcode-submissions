class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        N = len(nums)
        target = total // 2

        # 2D cache for i and sum1
        cache = [[-1] * (target + 1) for _ in range(N)]

        def dfs(i, sum1):
            if sum1 == target and i >= len(nums):
                return True
            if sum1 > target or i >= len(nums):
                return False 

            if cache[i][sum1] != -1:
                return cache[i][sum1]

            include = dfs(i + 1, sum1 + nums[i])
            exclude = dfs(i + 1, sum1)
            cache[i][sum1] = include or exclude

            return cache[i][sum1]

        return dfs(0, 0)
        