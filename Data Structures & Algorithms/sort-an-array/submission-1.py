class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m + 1, r)
            merge(l, m, r)

        def merge(l, m, r):
            left, right = nums[l:m+1], nums[m+1:r+1]
            l1, l2 = len(left), len(right)
            i, j, k = 0, 0, l
            while i < l1 and j < l2:
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < l1:
                nums[k] = left[i]
                i += 1
                k += 1

            while j < l2:
                nums[k] = right[j]
                j += 1
                k += 1

        mergeSort(0, len(nums) - 1)
        return nums