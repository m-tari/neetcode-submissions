from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, comb):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return
            for c in mp[digits[i]]:
                comb.append(c)
                backtrack(i + 1, comb)
                comb.pop()  # backtrack

        if digits:
            backtrack(0, [])
        
        return res
