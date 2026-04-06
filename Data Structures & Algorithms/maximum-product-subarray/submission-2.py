class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        maxSoFar = minSoFar = maxProd = nums[0]
        for i, num in enumerate(nums[1:]):
            if not num:
                maxProd = max(maxProd, num)
                maxSoFar = minSoFar = 1
                continue
            if num < 0:
                maxSoFar, minSoFar =  minSoFar, maxSoFar
            maxSoFar = max(num, maxSoFar * num)
            minSoFar = max(num, minSoFar * num)

            maxProd = max(maxSoFar, maxProd)
        return maxProd
        