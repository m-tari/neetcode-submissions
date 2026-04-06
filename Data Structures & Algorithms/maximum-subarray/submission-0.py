class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = 0
        currSum = 0
        maxSum = nums[0]

        for R in range(len(nums)):

            if currSum < 0:
                currSum = 0
                L = R

            currSum += nums[R]
            if currSum > maxSum:
                maxSum = currSum
        
        return maxSum

