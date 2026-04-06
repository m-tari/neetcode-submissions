class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return 1

        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# x*1 + y*2 = n


# n = 3
# ------
# x = 1, y = 1
# x = 3, y = 0

# ChatGPT said:

# This is a classic dynamic programming problem, often referred to as the Climbing Stairs problem.
# Problem Recap:

# You can take 1 or 2 steps at a time. Given n, return the number of distinct ways to reach the top.
# Observation:

# Let’s define f(n) as the number of ways to reach the n-th step.

#     To reach step n, you could:

#         Come from step n-1 by taking 1 step

#         Come from step n-2 by taking 2 steps

# So, the recurrence is:

#     f(n) = f(n-1) + f(n-2)

# With base cases:

#     f(0) = 1 (1 way to stay at the base)

#     f(1) = 1 (1 way to take one step)

# This is essentially the Fibonacci sequence, offset by 1.