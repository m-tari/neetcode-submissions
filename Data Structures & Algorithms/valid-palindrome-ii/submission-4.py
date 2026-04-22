class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1

        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while l <= r:
            if s[l] != s[r]:
                return is_palindrome(l, r - 1) or is_palindrome(l + 1, r)
            l += 1
            r -= 1 
                
        return True