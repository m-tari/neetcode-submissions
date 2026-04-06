class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        def merge(left, right):
            l, r = 0, 0
            m , n = len(left), len(right)
            res = []
            while l < m and r < n:
                if left[l] < right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            while l < m:
                res.append(left[l])
                l += 1

            while r < n:
                res.append(right[r])
                r += 1

            return res

        l = len(nums)
        m = l // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])
        sroted_array = merge(left, right)
        return sroted_array