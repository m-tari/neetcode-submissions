class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        maxSum = float('-inf')

        while i < n:
            sums = 0
            for j in range(i, i + n):
                sums += nums[j % n]
                maxSum = max(maxSum, sums)
                if sums < 0:
                    i = j
                    break
            i += 1

        return maxSum
