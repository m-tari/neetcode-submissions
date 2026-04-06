class Solution:
    def integerBreak(self, n: int) -> int:

            if n == 2:
                return 1  # 1 + 1 = 2 -> 1 x 1

            if n == 3:
                return 2  # 1 + 2 = 3 -> 1 x 2
        
            n3 = n // 3
            r3 = n % 3
            n2 = 0
            if r3 == 1:
                n3 -= 1
                n2 = 2
            elif r3 == 2:
                n2 = 1

            return 3 ** n3 * 2 ** n2

        # Example:

        # n = 12

        # 6 + 6     ->   36

        # 7 + 5     -> 35

        # 6 + 3 + 2 + 1  ->  36

        # 3 + 3 + 3 + 3  -> 81     ---> Max
 
        # 2 + 2 + 2 + 2 + 2 + 2  -> 64    


        # n = n3 * 3 + n2 * 2

        # We want to maximize the number of 3's first, and if there is something remaining, add 2's.

