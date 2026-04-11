class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # We iterate through the array, and for each element, 
        # if it's a valid positive number in range [1, n] 
        # and not already in its correct position, we swap it to where it belongs. 

        # Example:
        # nums = [3, 4, -1, 1]
        # We want:
        # index:  0  1  2  3
        # value:  1  2  3  4

        for i in range(n):
            # Each nums[i] should be at nums[i] - 1 index. We swap the nums until the condition is met.
            # if the value is already equal to the value of that position, we skip swapping.
            while 1 <= nums[i] <= n:
                correct_idx = nums[i] - 1

                # Skip swapping to avoid infinite loop
                if nums[i] == nums[correct_idx]:
                    break

                nums[correct_idx], nums[i] = nums[i], nums[correct_idx]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


