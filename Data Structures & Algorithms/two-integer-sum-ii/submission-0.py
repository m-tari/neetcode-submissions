class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            if numbers[r] > target - numbers[l]:
                r -= 1
            elif numbers[r] < target - numbers[l]:
                l += 1
            else:
                return [l + 1, r + 1]

                