class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i = x + 1
        candidate = x
        numMembers = 1

        while numMembers < n:
            if i & x == x:
                candidate = i
                numMembers += 1
            i += 1

        return candidate