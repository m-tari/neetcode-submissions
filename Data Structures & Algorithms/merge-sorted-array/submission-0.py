class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1

        while i >= 0 or j >= 0:
            num1 = nums1[i] if i >= 0 else float("-inf")
            num2 = nums2[j] if j >= 0 else float("-inf")
            k = i + j + 1

            if num1 > num2 :
                nums1[k] = num1
                i -= 1
            else:
                nums1[k] = num2
                j -= 1
