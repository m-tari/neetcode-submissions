from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # Minimum must be in the right half
                l = mid + 1
            else:
                # Minimum is at mid or in the left half
                r = mid

        return nums[l]
