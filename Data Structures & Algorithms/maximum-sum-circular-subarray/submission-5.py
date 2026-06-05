class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        curMax, curMin = 0, 0
        globMax, globMin =  nums[0],  nums[0]

        for num in nums:
            curMax = max(num, curMax + num)
            curMin = min(num, curMin + num)

            globMax = max(curMax, globMax)
            globMin = min(curMin, globMin)

        # all numbers are negative
        if globMax < 0:
            return globMax

        return max(globMax, total - globMin)