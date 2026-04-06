class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
            
        neg = True if x < 0 else False
        x = abs(x)
        r = 0
        while x:
            d = x % 10
            x = x // 10
            if x:
                r = r * 10 + d * 10
            else:
                r += d
            if -2**31 > r or r > 2**31 - 1:
                return 0

        return r if not neg else -r
