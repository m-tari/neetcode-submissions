class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = - 2 ** 31
            
        sign = -1 if x < 0 else 1
        r = 0
        x = abs(x)
        while x:
            d = x % 10
            x = x // 10
            if r > MAX // 10 or -r < MIN // 10 :
                return 0
            r = r * 10 + d

        return sign * r
