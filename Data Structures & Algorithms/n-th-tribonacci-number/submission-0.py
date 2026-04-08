class Solution:
    def tribonacci(self, n: int) -> int:
        T0, T1, T2 = 0, 1, 1

        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            for _ in range(3, n + 1):
                T0, T1, T2 = T1, T2, T0 + T1 + T2

            return T2
