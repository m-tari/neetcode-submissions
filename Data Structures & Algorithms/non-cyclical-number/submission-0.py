class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def process(n):
            s = 0
            while n:
                d = n % 10 
                n = n // 10
                s += d ** 2
            return s

        while n not in seen:
            n = process(n)
            seen.add(n)
            if n == 1:
                return True
        
        return False



 #       223 = 2 *10 ** 2 + 2 * 10 ** 1 + 3 * 10 ** 0