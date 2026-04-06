class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # There are n items in nums (0,..,n are n + 1 items, but one is missing so n items in nums)
        # Init res with n so that we can use for loop and return the value,
        # Otherwise we had to init res with 0 and add len(nums) after for loop
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res