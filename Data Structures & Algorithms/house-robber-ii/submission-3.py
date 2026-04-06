class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(arr):
            dp = [0] * (n - 1)
            dp[0] = arr[0]
            dp[1] = max(dp[0], arr[1])

            # Skip i means we use results of previous max rob (dp[i - 1])
            # Include i means we use the results of max rob before previous (dp[i - 2]) plus arr[i]
            for i in range(2, n - 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[-1]

        return max(solve(nums[1:]), solve(nums[:-1])) 