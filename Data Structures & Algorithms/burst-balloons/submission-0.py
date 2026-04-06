class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums:
            return 0

        if n == 1:
            return nums[0]

        nums_r = nums[1: n - 1]
        res = 0

        while nums_r:
            min_item = min(nums_r)
            min_index_r = nums_r.index(min_item)
            min_index = min_index_r + 1
            res += nums[min_index - 1]* nums[min_index] * nums[min_index + 1]
            nums_r.pop(min_index_r)
            nums.pop(min_index)

        if nums[0] > nums[1]:
            res += nums[0] * nums[1] + nums[0]
        else:
            res += nums[0] * nums[1] + nums[1]

        return res
            