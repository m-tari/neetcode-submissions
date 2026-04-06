class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res

    # Why it’s O(n):

    # even though the while loop is nested inside the for loop, 
    # each element in nums is added to the total once (via r) 
    # and removed from the total once (via l). Therefore, l and r each move at most n times.

    # Both pointers (l and r) traverse the array at most once.

    # Total operations across both loops is at most 2n — still linear.