class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0


        length = len(nums) + 1

        for l in range(len(nums)):
            curSum = 0
            for r in range(l, len(nums)):
                curSum += nums[r]
                if curSum >= target:
                    length = min(length, r - l + 1)
                    

        return length if length != len(nums) + 1 else 0


            

        