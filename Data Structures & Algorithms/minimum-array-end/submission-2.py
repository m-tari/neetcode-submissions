class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ###
        # Two pointer approach
        ###
        res = x
        i_x = 1  # Pointer for x
        i_n = 1  # Pointer for n - 1
        
        # x is always the first number in the array.
        # In order to the get last number in the array, we fill the zeros in x
        # with bits from n - 1, which is going to give us the nth number in the array.
        # Since all the available blanks are already zero, we only move the bit from n-1 to x
        # if it's 1, i. e: if i_n & (n - 1)

        #                  i_n
        # n - 1 :   1 0 1 0 0
        #                    / | |
        #                  v   v v
        # x      :    _ _ 1 _ _
        #                i_x

        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res = res | i_x
                i_n = i_n << 1
            i_x = i_x << 1

        return res

        # T: O(log(n))
        # Add each bit doubles the larget value you can present with that bits
        #
        # Max value woth k bits = 2^k - 1
        # 1 bit → max value = 1
        # 2 bits → max value = 3
        # 3 bits → max value = 7
        # 4 bits → max value = 15
        #
        # To represent a number n, you need enough bits k such that:
        # 2^k - 1 > n
        # So the number of bits for a number n
        # k > log_2 (n + 1)

        # S: O(1)