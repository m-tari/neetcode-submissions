class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (i, summation)

        def dfs(i, summation):
            if i == len(nums):
                return 1 if summation == target else 0
            if (i, summation) in dp:
                return dp[(i, summation)]

            dp[(i, summation)] = (
                dfs(i + 1,  nums[i] + summation) +
                dfs(i + 1, -nums[i] + summation)
            )

            return dp[(i, summation)]                

        return dfs(0, 0)

# nums = [1, 1, 1]
# target = 1

# Recursion Tree (partial)

# We start from i = 0, total = 0.

#                 (0, 0)
#                /      \
#         +1 -> /        \ <- -1
#            (1, 1)     (1, -1)
#           /    \      /     \
#    +1 -> /      \    /       \ <- -1
#       (2, 2)  (2, 0) (2, 0)  (2, -2)

# Notice the Overlap

#     From (0, 0), going:

#         Right → (1, -1) → Left → (2, 0)

#         Left → (1, 1) → Right → (2, 0)

# So (2, 0) is reached in two different ways:

#     First: +1 → -1

#     Second: -1 → +1

# In both cases, we're at index 2, and the total is 0.

# Without memoization, we’d compute the rest of the recursion twice from (2, 0).
# With memoization, the second call just reuses the stored result.



        