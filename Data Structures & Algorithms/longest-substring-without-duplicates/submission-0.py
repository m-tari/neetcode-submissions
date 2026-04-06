class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        charS = set()
        res = 0

        for r in range(n):
            while s[r] in charS:
                charS.remove(s[l])
                l += 1
            charS.add(s[r])
            res = max(res, r - l + 1)
        
        return res