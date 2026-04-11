class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # Each nums[i] should be in nums[i] - 1 position. We swap the nums until the condition is met.
            # if the value is already equal to the value of that position, we skip swapping.
            while 1 <= nums[i] <= n:
                correct_idx = nums[i] - 1

                if nums[i] == nums[correct_idx]:
                    break

                nums[correct_idx], nums[i] = nums[i], nums[correct_idx]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


