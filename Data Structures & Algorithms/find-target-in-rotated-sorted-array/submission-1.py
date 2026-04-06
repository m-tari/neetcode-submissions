class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m =(l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        if target < nums[pivot]:
            l, r = 0, pivot - 1
        else:
            l, r = pivot, n - 1

        while l <= r:
            m =(l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1


# [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]