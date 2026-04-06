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
