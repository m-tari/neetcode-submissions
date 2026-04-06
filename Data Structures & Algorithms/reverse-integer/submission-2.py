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
            if r * 10 + d > 2**31 - 1:
                return 0
            r = r * 10 + d

        return r if not neg else -r
