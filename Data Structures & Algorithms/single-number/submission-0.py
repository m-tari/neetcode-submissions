class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None

        x = nums[0]
        for i in range(1, len(nums)):
            x ^= nums[i]

        return x