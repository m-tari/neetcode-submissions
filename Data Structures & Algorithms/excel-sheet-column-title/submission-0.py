import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mp = {i: ch for i, ch in enumerate(string.ascii_uppercase)}
        base = len(mp)
        res = ""
        while columnNumber:
            columnNumber -= 1
            d = columnNumber % base
            res += mp[d]
            columnNumber = columnNumber // base

        return res[::-1]