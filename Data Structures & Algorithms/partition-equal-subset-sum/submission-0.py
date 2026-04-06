class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sum1 = 0
        sum2 = 0

        def dfs(i, sum1, sum2):
            if sum1 == sum2 and i >= len(nums):
                return True
            if sum1 != sum2 and i >= len(nums):
                return False 

            # In sum1
            if dfs(i + 1, sum1 + nums[i], sum2):
                return True

            # In sum2
            if dfs(i + 1, sum1, sum2 + nums[i]):
                return True

            return False

        return dfs(0, sum1, sum2)
        