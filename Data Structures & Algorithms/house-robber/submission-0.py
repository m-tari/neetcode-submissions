class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max_sum = 0

        def dfs(i):
            if i >= len(nums):
                return 0
            return nums[i] + dfs(i+2)

        for i in range(len(nums)):
            sum = nums[i] + dfs(i+2)
            if sum > max_sum:
                max_sum = sum

        return max_sum
