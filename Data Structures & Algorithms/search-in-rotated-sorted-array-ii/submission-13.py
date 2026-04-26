class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1

        # Find pivot (index of smallest element)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[l]:
                l = m
            elif nums[m] < nums[l]:
                r = m
            else:
                l += 1   # handle duplicates safely

        pivot = l

        # Decide which half to search
        l, r = 0, n - 1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        # Standard binary search
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False