class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max_sum = 0

        def dfs(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i+2), dfs(i+1))

        for i in range(len(nums)):
            sum = nums[i] + dfs(i+2)
            if sum > max_sum:
                max_sum = sum

        return max_sum
