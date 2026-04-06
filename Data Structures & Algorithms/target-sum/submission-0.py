class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summation = 0

        def dfs(i, summation):
            if i == len(nums):
                return 1 if summation == target else 0

            return (
                dfs(i + 1,  nums[i] + summation) +
                dfs(i + 1, -nums[i] + summation)
            )                

        return dfs(0, 0)






        