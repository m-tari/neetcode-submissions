
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
            # Since we are working with positive values and the limit for 
            # positive values is more strict, we can simply check the MAX limit.
            # (If a MIN limit is hit, it's alreay hit the MAX anyway.)
            if r > MAX // 10 or (r == MAX // 10 and d > MAX % 10):
                return 0
            r = 10 * r + d
        return sign * r
